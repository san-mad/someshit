
// Глитч-буквы для обычного HTML
// Глитч-буквы для обычного HTML
(function () {
  // Настройки
  const glitchColors = ['#099132ff', '#00ff15ff', '#0c7c00ff'];
  const glitchSpeed = 0;
  const smooth = true;
  const fontSize = 18;
  const charWidth = 10;1
  const charHeight = 20;
  const lettersAndSymbols = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    '!', '@', '#', '$', '%', '^', '&', '*', '(',
    ')', '-', '_', '=', '+', '{', '}', '[', ']', '|',
    ':', ';', '"', "'", '<', '>', ',', '.', '?', '/',
    '~', '`', ' ', '\n', '\t'
  ];

  // Создать canvas на фоне
  function createCanvas() {
    const canvas = document.createElement('canvas');
    canvas.id = 'glitch-bg-canvas';
    canvas.style.position = 'fixed';
    canvas.style.top = '0';
    canvas.style.left = '0';
    canvas.style.width = '110vw';
    canvas.style.height = '110vh';
    canvas.style.zIndex = '-1';
    canvas.style.display = 'block';
    canvas.style.background = '#000000ff';
    document.body.appendChild(canvas);
    return canvas;
  }

  function getRandomChar() {
    return lettersAndSymbols[Math.floor(Math.random() * lettersAndSymbols.length)];
  }
  function getRandomColor() {
    return glitchColors[Math.floor(Math.random() * glitchColors.length)];
  }
  function hexToRgb(hex) {
    const shorthandRegex = /^#?([a-f\d])([a-f\d])([a-f\d])$/i;
    hex = hex.replace(shorthandRegex, (m, r, g, b) => r + r + g + g + b + b);
    const result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
    return result ? {
      r: parseInt(result[1], 16),
      g: parseInt(result[2], 16),
      b: parseInt(result[3], 16)
    } : null;
  }
  function interpolateColor(start, end, factor) {
    const result = {
      r: Math.round(start.r + (end.r - start.r) * factor),
      g: Math.round(start.g + (end.g - start.g) * factor),
      b: Math.round(start.b + (end.b - start.b) * factor)
    };
    return `rgb(${result.r}, ${result.g}, ${result.b})`;
  }

  // Основная логика
  let canvas, ctx, grid, letters, lastGlitchTime, animationFrame;
  // Для "дождика" из надписей 'lain'
  const lainCount = 30
  const lainFontSize = 24;
  const lainAlpha = 0.6;
  let lainDrops = [];
  function initializeLainDrops() {
    lainDrops = [];
    for (let i = 0; i < lainCount; i++) {
      lainDrops.push({
        x: Math.random() * canvas.width,
        y: Math.random() * canvas.height
      });
    }
  }

  function calculateGrid(width, height) {
    const columns = Math.ceil(width / charWidth);
    const rows = Math.ceil(height / charHeight);
    return { columns, rows };
  }
  function initializeLetters(columns, rows) {
    grid = { columns, rows };
    const totalLetters = columns * rows;
    letters = Array.from({ length: totalLetters }, () => ({
      char: getRandomChar(),
      color: getRandomColor(),
      targetColor: getRandomColor(),
      colorProgress: 1
    }));
  }
  function resizeCanvas() {
    const dpr = window.devicePixelRatio || 1;
    canvas.width = window.innerWidth * dpr;
    canvas.height = window.innerHeight * dpr;
    canvas.style.width = window.innerWidth + 'px';
    canvas.style.height = window.innerHeight + 'px';
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    const { columns, rows } = calculateGrid(window.innerWidth, window.innerHeight);
    initializeLetters(columns, rows);
    initializeLainDrops();
    drawLetters();
  }
  function drawLetters() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.font = fontSize + 'px monospace';
    ctx.textBaseline = 'top';
    for (let i = 0; i < letters.length; i++) {
      const x = (i % grid.columns) * charWidth;
      const y = Math.floor(i / grid.columns) * charHeight;
      ctx.fillStyle = letters[i].color;
      ctx.fillText(letters[i].char, x, y);
    }
    // Рисуем много маленьких полупрозрачных 'lain', которые движутся в разные стороны
    ctx.save();
  ctx.font = `lighter ${lainFontSize}px Arial`;
    ctx.fillStyle = `rgba(255,0,0,${lainAlpha})`;
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    for (let i = 0; i < lainDrops.length; i++) {
      ctx.fillText('lain', lainDrops[i].x, lainDrops[i].y);
    }
    ctx.restore();
  }
  function updateLetters() {
    const updateCount = Math.max(1, Math.floor(letters.length * 0.05));
    for (let i = 0; i < updateCount; i++) {
      const index = Math.floor(Math.random() * letters.length);
      letters[index].char = getRandomChar();
      letters[index].targetColor = getRandomColor();
      if (!smooth) {
        letters[index].color = letters[index].targetColor;
        letters[index].colorProgress = 1;
      } else {
        letters[index].colorProgress = 0;
      }
    }
  }
  function handleSmoothTransitions() {
    let needsRedraw = false;
    for (let i = 0; i < letters.length; i++) {
      if (letters[i].colorProgress < 1) {
        letters[i].colorProgress += 0.05;
        if (letters[i].colorProgress > 1) letters[i].colorProgress = 1;
        const startRgb = hexToRgb(letters[i].color);
        const endRgb = hexToRgb(letters[i].targetColor);
        if (startRgb && endRgb) {
          letters[i].color = interpolateColor(startRgb, endRgb, letters[i].colorProgress);
          needsRedraw = true;
        }
      }
    }
    if (needsRedraw) drawLetters();
  }
  function animate() {
    const now = Date.now();
    if (now - lastGlitchTime >= glitchSpeed) {
      updateLetters();
      // Телепортируем lainDrops в новые случайные точки
      for (let i = 0; i < lainDrops.length; i++) {
        lainDrops[i].x = Math.random() * canvas.width;
        lainDrops[i].y = Math.random() * canvas.height;
      }
      drawLetters();
      lastGlitchTime = now;
    }
    if (smooth) handleSmoothTransitions();
    animationFrame = requestAnimationFrame(animate);
  }

  function startGlitchBackground() {
    canvas = document.getElementById('glitch-bg-canvas') || createCanvas();
    ctx = canvas.getContext('2d');
    lastGlitchTime = Date.now();
    resizeCanvas();
    animate();
    window.addEventListener('resize', function () {
      cancelAnimationFrame(animationFrame);
      resizeCanvas();
      animate();
    });
  }

  // Запуск после загрузки страницы
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', startGlitchBackground);
  } else {
    startGlitchBackground();
  }
})();
    
