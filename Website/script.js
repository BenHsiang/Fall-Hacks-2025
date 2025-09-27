window.addEventListener('load', () => {
  const splash = document.getElementById('splash-screen');
  
  // Wait 2 seconds, then fade out the splash
  setTimeout(() => {
    splash.style.opacity = '0';

    // After transition ends, hide the splash completely
    splash.addEventListener('transitionend', () => {
      splash.style.display = 'none';
    });
  }, 2000); // 2000ms = 2 seconds splash visible
});
