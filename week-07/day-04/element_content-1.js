// 1
var heading = document.querySelectorAll('h1');
window.alert(heading[0].innerHTML);

// 2
var first_p = document.querySelectorAll('p:nth-of-type(1)');
console.log(first_p[0].innerHTML);

// 3
var second_p = document.querySelectorAll('.other');
window.alert(second_p[0].innerHTML);

// 4
heading[0].innerHTML = 'New content';

// 5
var paragraphs = document.querySelectorAll('p');
paragraphs[2].innerHTML = paragraphs[0].innerHTML;
