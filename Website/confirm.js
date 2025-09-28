 const API = "http://127.0.0.1:8000"; // FastAPI endpoint (make sure CORS is enabled in dev)
    let x = 0;
    let problemId = null;
    let selectedItems = [];
    let total = 0;
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
    if (!raw) { 
        document.getElementById('order').textContent = "No order data."; 
        selectedItems = [];
        total = 0;
        return;     
    }
    const data = JSON.parse(raw);
    selectedItems = data.items || [];
    total = Number(data.total || 0);
    const names = selectedItems.map(i => i.title).join(', ');
    document.getElementById('order').textContent = `Items: ${names || '(none)'}  |  Total: $${total.toFixed(2)}`;
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
    if (!problemId) return alert('No question loaded yet.');
    const user_answer = document.getElementById('ans').value.trim();
    if (!user_answer) return alert('Type your answer first.');

    const btn = document.getElementById('check');
    btn.disabled = true;
    try {
      const r = await fetch(`${API}/calc1/check`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ id: problemId, user_answer})
      });
      const data = await r.json();

      // Update attempts display if present
      if (typeof data.attempts_left === 'number') {
        document.getElementById('attempts').textContent =
          `Attempts left: ${data.attempts_left}`;
      }

      const resultEl = document.getElementById('result');
      resultEl.textContent = data.correct
        ? `✅ Correct!`
        : `❌ ${data.message}`;
      resultEl.className = data.correct ? 'ok' : 'bad';
      if (!data.correct) {
        x += 1;
      }
      
      if (data.correct || data.attempts_left <= 0) {
        total += x*10

        localStorage.setItem('order', JSON.stringify({
            items: selectedItems,
            total: total,
            x : x
        }));
        window.location.href = 'display.html';
      }
    } catch (e) {
      document.getElementById('result').textContent = 'Check failed.';
      console.error(e);
    } finally {
      btn.disabled = false;
    }
  }

    document.getElementById('check').addEventListener('click', checkAnswer);

    // On load
    (async () => {
      await loadOrder();
      await getQuestion();
    })();