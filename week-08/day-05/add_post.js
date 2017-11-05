'use strict';

const postData = {
    "title": "",
    "url": ""
}

function post(data) {
    let xhr = new XMLHttpRequest();
    xhr.open('POST', 'http://secure-reddit.herokuapp.com/simple/posts');
    xhr.setRequestHeader('Content-type', 'application/json');
    xhr.onload = function() {
        console.log(this.responseText);
    }
    xhr.send(data);
}

let postButton = document.querySelector('button');
postButton.addEventListener('click', function() {
    postData.title = document.querySelector('input.title').value;
    postData.url = document.querySelector('input.url').value;
    console.log(postData);
    if ( postData.title !== '') {
        post(postData);                 //results error 400
        // window.location.href = 'main.html'     //redirects back to main page
    } else {
        alert('Please don\'t let the title field empty');
    }
});