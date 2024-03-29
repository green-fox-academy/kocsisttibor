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
        <a href=#><div class = "up_${data.posts[i].id}"></div></a>
        <div class = "score_${data.posts[i].id}">${data.posts[i].score}</div>
        <a href=#><div class = "down_${data.posts[i].id}"></div></a>
        </div>
        <article>
        <a href=${data.posts[i].url}><div>${data.posts[i].title}</div></a>
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
        container.appendChild(section);
        let upArrow = document.querySelector('div.up_' + data.posts[i].id);
        upArrow.addEventListener('click', callVote);
        let downArrow = document.querySelector('div.down_' + data.posts[i].id);
        downArrow.addEventListener('click', callVote);
    }
    let loading = document.querySelector('p.loading');
    loading.style.display = 'None';
}

function callVote() {
    vote(this.className, response => {
        let className = 'score_' + this.className.split('_')[1];
        let scoreDiv = document.querySelector('div.' + className);
        scoreDiv.innerHTML = response.score;
    });
    this.className.includes('up') ? 
        this.style.backgroundImage = 'url(css/upvoted.png)':
        this.style.backgroundImage = 'url(css/downvoted.png)';
}

function vote(id, callback) {
    let xhr = new XMLHttpRequest();
    xhr.open('PUT', 'http://localhost:8080/posts/' + id);
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE) {       //same as xhr.readystate === 4
            callback(JSON.parse(xhr.response))
        }
    }
    xhr.send();
}

window.onload = getPosts(createSection);
