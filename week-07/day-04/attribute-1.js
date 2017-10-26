var image = document.querySelector('img');
console.log(image.getAttribute('src'))

image.setAttribute('src', 'http://images.mentalfloss.com/sites/default/files/styles/insert_main_wide_image/public/istock_000048297906_small.jpg');

var link = document.querySelector('a');

link.setAttribute('href', 'https://www.greenfoxacademy.com')

var button = document.querySelector('.this-one');

button.disabled = true;
button.textContent = 'Don\'t click me!'