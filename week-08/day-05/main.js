'use strict';
function getPosts(callback) {
    let xhr = new XMLHttpRequest();
    xhr.open('GET', 'http://secure-reddit.herokuapp.com/simple/posts');
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4) {
            callback(JSON.parse(xhr.responseText));
        }
    }
    xhr.send();
}

function createSection (data) {
    for (let i = 0; i < data.posts.length; i += 1) {
        let structure = `
            <div class = "vote_block">
                <div></div>
                <div>${data.posts[i].score}</div>
                <div></div>
            </div>
            <article>
                <div>${data.posts[i].title}</div>
                <div>${data.posts[i].user}</div>
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
    let loading = document.querySelector('p.loading');
    loading.style.display = 'None';
}

window.onload = getPosts(createSection);
