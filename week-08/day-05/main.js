'use strict';
function getPosts(callback) {
    let xhr = new XMLHttpRequest();
    xhr.open('GET', 'https://cors-anywhere.herokuapp.com/http://secure-reddit.herokuapp.com/posts');
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4) {
            callback(JSON.parse(xhr.responseText));
        }
    }
    xhr.send();
}

function createSection (data) {
    let structure = `
        <div class = "vote_block">
            <div></div>
            <div>2.342</div>
            <div></div>
        </div>
        <article>
            <div>post</div>
            <div>owner</div>
            <ul>
                <li>comments</li>
                <li>modify</li>
                <li>remove</li>
            </ul>
        </article>
    `
    let container = document.querySelector('container.left');
    let section = document.createElement('section');
    section.innerHTML = structure;
    container.appendChild(section)
}
createSection()
// window.onload = getPosts(createPosts);
