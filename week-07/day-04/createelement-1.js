var ul = document.querySelector('ul');
var newLi = document.createElement('li');
var newLi_2 = document.createElement('li');
var heading = document.createElement('p');
var body = document.querySelector('body');
var img = document.createElement('img');

newLi.textContent = 'The Green Fox';
newLi_2.textContent = 'The Lamplighter';

ul.appendChild(newLi);
ul.appendChild(newLi_2);

heading.textContent ='I can add elements to the DOM!'

body.insertBefore(heading, ul);

img.setAttribute('src', 'https://image.spreadshirtmedia.com/image-server/v1/mp/products/T268A544MPA392PT10X2Y0D1010571922S27/views/1,width=1200,height=1200,appearanceId=544,backgroundColor=E8E8E8/cobra-pose-unicorn-exhale-outline-contrast-coffee-mug.webp')
body.insertAfter(img, ul);