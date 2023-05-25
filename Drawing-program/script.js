window.addEventListener('load', () => {
  const canvas = document.getElementById('canvas');
  const context = canvas.getContext('2d');
  const uploadInput = document.getElementById('uploadInput');
  let isDrawing = false;
  let currentColor = 'black';
  let brushSize = 5;

  // Set up event listeners
  canvas.addEventListener('mousedown', startDrawing);
  canvas.addEventListener('mousemove', draw);
  canvas.addEventListener('mouseup', stopDrawing);
  canvas.addEventListener('mouseout', stopDrawing);

  const clearButton = document.getElementById('clearButton');
  clearButton.addEventListener('click', clearCanvas);

  const smallButton = document.getElementById('smallButton');
  smallButton.addEventListener('click', smallBrush);

  const mediumButton = document.getElementById('mediumButton');
  mediumButton.addEventListener('click', mediumBrush);

  const largeButton = document.getElementById('largeButton');
  largeButton.addEventListener('click', largeBrush);

  const pinkButton = document.getElementById('pinkButton');
  pinkButton.addEventListener('click', setPinkColor);

  const redButton = document.getElementById('redButton');
  redButton.addEventListener('click', setRedColor);

  const orangeRedButton = document.getElementById('orangeRedButton');
  orangeRedButton.addEventListener('click', setOrangeRedColor);

  const orangeButton = document.getElementById('orangeButton');
  orangeButton.addEventListener('click', setOrangeColor);

  const yellowButton = document.getElementById('yellowButton');
  yellowButton.addEventListener('click', setYellowColor);

  const yellowGreenButton = document.getElementById('yellowGreenButton');
  yellowGreenButton.addEventListener('click', setYellowGreenColor);

  const greenButton = document.getElementById('greenButton');
  greenButton.addEventListener('click', setGreenColor);

  const lightBlueButton = document.getElementById('lightBlueButton');
  lightBlueButton.addEventListener('click', setLightBlueColor);

  const blueButton = document.getElementById('blueButton');
  blueButton.addEventListener('click', setBlueColor);

  const purpleButton = document.getElementById('purpleButton');
  purpleButton.addEventListener('click', setPurpleColor);

  const brownButton = document.getElementById('brownButton');
  brownButton.addEventListener('click', setBrownColor);

  const blackButton = document.getElementById('blackButton');
  blackButton.addEventListener('click', setBlackColor);

  const greyButton = document.getElementById('greyButton');
  greyButton.addEventListener('click', setGreyColor);

  const whiteButton = document.getElementById('whiteButton');
  whiteButton.addEventListener('click', setWhiteColor);

  uploadInput.addEventListener('change', function (e) {
    const file = e.target.files[0];
    const reader = new FileReader();
  
    reader.onload = function (event) {
      const img = new Image();
      img.onload = function () {
        img.width = canvas.width;
        img.height = canvas.height;
        context.drawImage(img, 0, 0);
      };
      img.src = event.target.result;
    };
  
    reader.readAsDataURL(file);
  });

  function startDrawing(e) {
    isDrawing = true;
    draw(e);
  }

  function draw(e) {
    if (!isDrawing) return;

    const x = e.clientX - canvas.offsetLeft;
    const y = e.clientY - canvas.offsetTop;

    context.strokeStyle = currentColor;
    context.lineWidth = brushSize;

    context.lineTo(x, y);
    context.stroke();
  }

  function stopDrawing() {
    isDrawing = false;
    context.beginPath();
  }

  function clearCanvas() {
    context.clearRect(0, 0, canvas.width, canvas.height);
  }

  function smallBrush() {
    brushSize = 5;
  }

  function mediumBrush() {
    brushSize = 10;
  }

  function largeBrush() {
    brushSize = 20;
  }

  function setPinkColor() {
    currentColor = 'pink';
  }
  function setRedColor() {
    currentColor = 'red';
  }
  function setOrangeColor() {
    currentColor = 'orange';
  }
  function setOrangeRedColor() {
    currentColor = 'orangered';
  }
  function setYellowColor() {
    currentColor = 'yellow';
  }
  function setYellowGreenColor() {
    currentColor = 'yellowgreen';
  }
  function setGreenColor() {
    currentColor = 'green';
  }
  function setLightBlueColor() {
    currentColor = 'lightskyblue';
  }
  function setBlueColor() {
    currentColor = 'blue';
  }
  function setPurpleColor() {
    currentColor = 'purple';
  }
  function setBrownColor() {
    currentColor = '#964B00';
  }
  function setBlackColor() {
    currentColor = 'black';
  }
  function setGreyColor() {
    currentColor = 'grey';
  }
  function setWhiteColor() {
    currentColor = 'white';
  }
});
