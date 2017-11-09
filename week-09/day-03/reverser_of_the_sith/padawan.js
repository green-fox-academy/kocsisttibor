'use strict';

function getWisdoms() {
    console.log('started');
    let xhr = new XMLHttpRequest();
    xhr.open('POST', 'http://localhost:8080');
    xhr.send();
    console.log(xhr.responseText);
}

document.querySelector('button').addEventListener('click', getWisdoms)
