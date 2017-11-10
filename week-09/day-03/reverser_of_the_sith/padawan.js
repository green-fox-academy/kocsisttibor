'use strict';

function getWisdoms() {
    console.log('started');
    let xhr = new XMLHttpRequest();
    xhr.open('POST', 'http://localhost:8080');
    let input = document.querySelector('input').value;
    let data = {"text": input};
    console.log(data)
    xhr.send(data);
    // document.querySelector('div.answer').innerHTML = xhr.responseText;
    let answer = JSON.parse(xhr.responseText)
    console.log(answer);
}

document.querySelector('button').addEventListener('click', function() {
    document.querySelector('div.grr').style.display = 'block';
})
