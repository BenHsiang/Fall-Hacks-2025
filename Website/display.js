function getRandomInt(min, max) {
  min = Math.ceil(min); 
  max = Math.floor(max); 
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

let targetDate = new Date();
targetDate.setMinutes(targetDate.getMinutes() + getRandomInt(10, 30)); 

function updateCountdown() {
  let now = new Date(); 
  let timeRemaining = targetDate - now; 
  
  let minutes = Math.floor((timeRemaining % (1000 * 60 * 60)) / (1000 * 60));
  let seconds = Math.floor((timeRemaining % (1000 * 60)) / 1000);
  
  document.getElementById("timer").innerHTML = minutes + "m " + seconds + "s";

  if (timeRemaining < 0) {
    clearInterval(timerInterval); 
    document.getElementById("timer").innerHTML = "Order delivered!";
  }
}

let timerInterval = setInterval(updateCountdown, 1000);

async function loadOrder() {
    const raw = localStorage.getItem('order');
    if (!raw) { document.getElementById('order').textContent = "No order data."; return; }
    const data = JSON.parse(raw);
    const names = (data.items || []).map(i => i.title).join(', ');
    print(names);
    document.getElementById('order').textContent = `Items: ${names || '(none)'}  |  Total: $${(data.total||0).toFixed(2)}`;
}

(async () => {
    await loadOrder();
})();
