'use strict';
function getPosts(callback) {
    let xhr = new XMLHttpRequest();
    xhr.open('GET', 'http://localhost:8080/posts');
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4) {
            callback(JSON.parse(xhr.responseText));
        }
    }
    xhr.send();
}

function createSection (data) {
    console.log(data)
    for (let i = 0; i < data.posts.length; i += 1) {
        let timestamp = new Date(data.posts[i].timestamp);
        let now = new Date();
        let elapsed = new Date((now - timestamp));
        let author = data.posts[i].user === null ? 'anonymus': data.posts[i].user;
        let structure = `
            <div class = "vote_block">
                <div></div>
                <div>${data.posts[i].score}</div>
                <div></div>
            </div>
            <article>
                <div>${data.posts[i].title}</div>
                <div>submitted ${elapsed.getMinutes()} minutes ago by ${author}</div>
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
