 const API = "http://127.0.0.1:8000"; // FastAPI endpoint (make sure CORS is enabled in dev)

let problemId = null;

function renderAuto() {
    if (window.renderMathInElement) {
    renderMathInElement(document.body, {
        delimiters: [
        { left: "$$", right: "$$", display: true },
        { left: "\\[", right: "\\]", display: true },
        { left: "$",  right: "$",  display: false },
        ],
    });
    }
}

async function loadOrder() {
    const raw = localStorage.getItem('order');
    if (!raw) { document.getElementById('order').textContent = "No order data."; return; }
    const data = JSON.parse(raw);
    const names = (data.items || []).map(i => i.title).join(', ');
    document.getElementById('order').textContent = `Items: ${names || '(none)'}  |  Total: $${(data.total||0).toFixed(2)}`;
}

async function getQuestion() {
    const qEl = document.getElementById('q');
    qEl.textContent = '(loading question...)';
    try {
    // Optionally pass topic/difficulty via query params:
    // const r = await fetch(`${API}/calc1/next?topic=derivatives&difficulty=easy`);
    const r = await fetch(`${API}/calc1/next`);
    if (!r.ok) throw new Error(`HTTP ${r.status}`);
    const data = await r.json();
    problemId = data.id;

    // Ensure the question string is wrapped in math delimiters if needed
    const raw = data.q_latex || data.q || '';
    const toRender = /\$|\\\(|\\\[/.test(raw) ? raw : `$${raw}$$`;

    // Insert and render
    qEl.textContent = '';
    const span = document.createElement('span');
    span.textContent = toRender;     // safe text insertion
    qEl.appendChild(span);
    renderAuto();
    } catch (e) {
    qEl.textContent = 'Failed to load question.';
    console.error(e);
    }
}

async function checkAnswer() {
    attempt = 5;

    if (!problemId) return alert('No question loaded yet.');
    for(let i = 0; i < attempt; i++){
    const user_answer = document.getElementById('ans').value.trim();
    if (!user_answer) return alert('Type your answer first.');

    try {
        const r = await fetch(`${API}/calc1/check`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ id: problemId, user_answer, reveal_answer: true })
        });
        const data = await r.json();
        const resultEl = document.getElementById('result');
        resultEl.textContent = data.correct ? '✅ Correct' : '❌ Incorrect';
        resultEl.className = data.correct ? 'ok' : 'bad';
        
    } catch (e) {
        document.getElementById('result').textContent = 'Check failed.';
        console.error(e);
    }
    }
}

document.getElementById('check').addEventListener('click', checkAnswer);

// On load
(async () => {
    await loadOrder();
    await getQuestion();
})();