var child = document.querySelector('li:nth-of-type(1)');
var parent = document.querySelector('ul');

parent.removeChild(child);

var planetData = [
    {
      category: 'inhabited',
      content: 'Foxes',
      asteroid: true
    },
    {
      category: 'inhabited',
      content: 'Whales and Rabbits',
      asteroid: true
    },
    {
      category: 'uninhabited',
      content: 'Baobabs and Roses',
      asteroid: true
    },
    {
      category: 'inhabited',
      content: 'Giant monsters',
      asteroid: false
    },
    {
      category: 'inhabited',
      content: 'Sheep',
      asteroid: true
    }
]
planetData.forEach(function(e, i) {
    if (planetData[i].asteroid === true) {
        var newChild = document.createElement('li');
        parent.appendChild(newChild);
        newChild.textContent = planetData[i].content;
    }
});