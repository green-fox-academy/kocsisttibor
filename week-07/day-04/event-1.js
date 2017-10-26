var button = document.querySelector('button');
var body = document.querySelector('body');

function party () {
    body.classList.toggle('party');
}

button.addEventListener('click', party)