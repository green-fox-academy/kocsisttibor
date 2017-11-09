
'use strict';

const xml = new XMLHttpRequest();
const body = document.querySelector('body');
let url = "http://localhost:8080";

function talkToAPI(method, resource){
    xml.open(method, url + resource, true);
    xml.onload = function(){
        body.innerHTML = xml.response;
    }
    xml.send();
}

function getList(){
    talkToAPI('GET', '/titles')
}

getList();