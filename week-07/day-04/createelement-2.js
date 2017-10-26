var parent = document.querySelector('ul');
var child = document.querySelector('li:nth-of-type(1)');

parent.removeChild(child)

for (let i = 1; i < 17; i += 1) {
    var newChild = document.createElement('li');
    parent.appendChild(newChild);
    newChild.textContent = 'Empty box #' + i;
}
