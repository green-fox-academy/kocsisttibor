// 1
var newlist = ['apple', 'banana', 'cat', 'dog'];
var oldlist = document.querySelectorAll('li');

oldlist.forEach(function(x, i) {
    oldlist[i].innerHTML = newlist[i];
})


// 2
var ul_tag = document.querySelector('ul');

ul_tag.style.backgroundColor = "limegreen";