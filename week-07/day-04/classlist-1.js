var third_p = document.querySelector('p:nth-of-type(3)');

if (third_p.classList.contains('red-dot') === true) {
    window.alert('OMG DOTS!')
}

var paragraphs = document.querySelectorAll('p');

if (paragraphs[3].classList.contains('dolphin')) {
    paragraphs[0].innerHTML = 'pear';
}

if (paragraphs[0].classList.contains('apple')) {
    paragraphs[2].innerHTML = 'dog';
}

paragraphs[0].classList.add('red');

paragraphs[1].style.borderRadius = '10%';