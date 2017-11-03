'use strict';
function getPosts() {
    let xhr = new XMLHttpRequest();
    xhr.open('GET', 'https://cors-anywhere.herokuapp.com/http://secure-reddit.herokuapp.com/posts');
    xhr.onreadystate = function() {
        console.log(xhr.result)
        if (xhr.readyState === 4) {
            console.log(JSON.parse(xhr.responseText));
        }
    }
    xhr.send();
}

window.onload = getPosts();
