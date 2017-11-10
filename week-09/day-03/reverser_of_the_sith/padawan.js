'use strict';

function grabInput() {
    let input = document.querySelector('input').value;
    let data = {"text": input};
    return data;
}

function getWisdoms() {
    let xhr = new XMLHttpRequest();
    xhr.open('POST', 'http://localhost:8080');
    xhr.setRequestHeader('Content-type', 'application/json')
    let data = grabInput()
    xhr.onreadystatechange = function() {     //this part handles the asynchronity; otherwise response should have been used before it arrives
        
        if (xhr.readyState === 4 && xhr.status === 200) {
            let answer = JSON.parse(xhr.response);
            document.querySelector('div.grr').innerHTML = answer.sithtext;
        }
    }
    xhr.send(JSON.stringify(data));   //data is an object, needs to be converted into string      
}

document.querySelector('button').addEventListener('click', getWisdoms);



