from fastapi import FastAPI, Body, Query
from pydantic import BaseModel
import requests, json, uuid, time, re
import sympy as sp
from typing import Dict, Any
from fastapi.middleware.cors import CORSMiddleware
import random

x = 0
MAX_ATTEMPTS = 5
DIFF_LEVELS = ["easy", "medium"]
TOPICS = ["limits", "derivatives", "basic integrals"]
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "qwen2.5:7b-instruct"   # swap to a math-tuned 7B if you have one
app = FastAPI(title="Calc I Generator", version="1.2")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # dev: allow all; tighten later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory: id -> {q, topic, difficulty, answer, ts}
SESSION: Dict[str, Dict[str, Any]] = {}

def ollama_generate(prompt: str, temperature=0.4    , num_ctx=1536, num_predict=700) -> str:
    r = requests.post(
        OLLAMA_URL,
        json={"model": MODEL, "prompt": prompt,
              "options": {"temperature": temperature, "num_ctx": num_ctx, "num_predict": num_predict}},
        stream=True, timeout=180,
    )
    buf = ""
    for line in r.iter_lines():
        if not line: continue
        piece = json.loads(line.decode("utf-8"))
        buf += piece.get("response", "")
        if piece.get("done"): break
    print("Full response:", buf)
    return buf.strip()

def single_problem_prompt(topic=None, difficulty=None) -> str:
    # LaTeX examples with single backslashes (normal LaTeX)
    q_example  = r"Compute $\lim_{x\to 0} \frac{\sin(3x)}{x}$."
    q_example2 = r"$f(x) = x^2 \\sin(3x)$, find $f'(x)$."
    q_example3 = r"Compute $\int (2x^3 - 3x^2 + 4)\,dx$."

    # Turn them into proper JSON string literals (will contain \\ inside)
    q1j, q2j, q3j = (json.dumps(s) for s in (q_example, q_example2, q_example3))
    return f"""You are a Calculus I problem writer.
Return EXACTLY this JSON with one problem INCLUDING ONLY the solution (no steps).

{{
  "course": "Calculus I",
  "problem": {{
    "topic": "EXACTLY this topic: {topic}",
    "difficulty": "EXACTLY this difficulty: {difficulty}",
    "q": "A single well-formed question, e.g., {q1j} OR {q2j} OR {q3j}. Use x as the variable.",
    "answer": "Symbolic or numeric final answer (e.g., 3, e^x(2x+1), 0, ln|x|+C)."
  }}
}}

Rules:
- Keep at Calc I level.
- questions must be in the form stated above.
- Use Latex function names (e.g., \\sin, \\ln, \\int).
- STRICTLY Use LaTeX math mode (with $...$) for all math expressions.
- Prefer answers that are checkable (a number or a clean expression).
- Answers wil be in the form of plain text, e.g., 3, e^x(2x+1), 0, ln|x|+C.
- Answers will use ** for powers, e.g., x**2.
- Answers will use * for multiplication, e.g., x*2.
- For indefinite integrals, include +C.
- Output only the JSON object.
"""

def check_equivalence(correct: str, user: str) -> tuple[bool,str]:
    print(f"Checking: {correct} vs {user}")
    try:
        x = sp.symbols('x')
        correct_expr = sp.sympify(correct.replace('^', '**'))
        user_expr = sp.sympify(user.replace('^', '**'))
        if sp.simplify(correct_expr - user_expr) == 0:
            return True, "Correct!"
        else:
            return False, "Incorrect answer."
    except Exception as e:
        return False, f"Error in parsing expressions: {e}"
    

# --- API ---
@app.get("/calc1/next")
def next_problem():
    topic = random.choice(TOPICS)
    difficulty = random.choice(DIFF_LEVELS) 
    raw = ollama_generate(single_problem_prompt(topic,difficulty),temperature=0.5, num_ctx=1536, num_predict=700)
    data = json.loads(raw)
    p = data["problem"]
    print(p)
    prob_id = str(uuid.uuid4())
    SESSION[prob_id] = {
        "q": p["q"],
        "topic": p["topic"],
        "difficulty": p["difficulty"],
        "answer": p["answer"],
        "attempts": MAX_ATTEMPTS,
        "solved": False,
        "ts": time.time()
    }
    return {"id": prob_id, "topic": p["topic"], "difficulty": p["difficulty"], "q": p["q"]}

class CheckBody(BaseModel):
    id: str
    user_answer: str

@app.post("/calc1/check")
def check_answer(body: CheckBody = Body(...)):
    global x
    item = SESSION.get(body.id)
    if not item:
        return {"correct": False, "message": "Invalid or expired problem id."}
    if item["solved"]:
        return {"correct": True, "message": "Already solved."}
    if item["attempts"] <= 0:
        return {"correct": False, "message": "No attempts left.", "answer": item["answer"]}
    
    print(item["answer"], body.user_answer)
    ok, msg = check_equivalence(item["answer"], body.user_answer)
    if not ok:
        item["attempts"] -= 1
        if item["attempts"] <= 0:
            msg += f" No attempts left. The correct answer is: {item['answer']}"
        else:
            msg += f" You have {item['attempts']} attempts left."
    resp = {"correct": ok, "message": msg, "attempts_left": item["attempts"]}
    return resp
