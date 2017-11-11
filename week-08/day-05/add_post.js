'use strict';

const postData = {
    "title": "",
    "url": ""
}

function post(data, callback) {
    let xhr = new XMLHttpRequest();
    xhr.open('POST', 'http://localhost:8080/posts');
    xhr.setRequestHeader('Content-type', 'application/json');
    xhr.onload = function() {
        console.log('server\'s response: ' + this.response);
        callback();
    }
    xhr.send(JSON.stringify(data));   //string need to be sent to server, so first the objects shoulb be converted into string
}

const backToMainPage = () => window.location.href = 'main.html'     //redirects back to main page

let postButton = document.querySelector('button');
postButton.addEventListener('click', function() {
    postData.title = document.querySelector('input.title').value;
    postData.url = document.querySelector('input.url').value;
    if ( postData.title !== '') {
        post(postData, backToMainPage);
    } else {
        alert('Please don\'t let the title field empty');
    }
});