var button = document.querySelector('button');
var li_items = document.querySelectorAll('li');
var p = document.querySelector('p');

function answer() {
    p.textContent = li_items.length;
}

button.addEventListener('click', answer);

console.log(li_items.length)
