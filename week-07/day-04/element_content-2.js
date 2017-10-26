var paragraphs = document.querySelectorAll('p');
for (let i = 0; i < paragraphs.length - 1; i += 1) {
    paragraphs[i].innerHTML = paragraphs[paragraphs.length - 1].innerHTML;
}
