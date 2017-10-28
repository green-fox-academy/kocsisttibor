let images = [
    {'title':'Pumpkins', 'desc': 'asdlkdslhasdasd', 'url':'images/helena-yankovska-416906.jpg'},
    {'title':'Coffee', 'desc': 'asdlkdslhasdasd', 'url':'images/alisa-anton-166247.jpg'},
    {'title':'Stairs', 'desc': 'asdlkdslhasdasd', 'url':'images/arturo-castaneyra-396439.jpg'},
    {'title':'Busket', 'desc': 'asdlkdslhasdasd', 'url':'images/aaron-burden-40485.jpg'},
    {'title':'Colorful pumpkins', 'desc': 'asdlkdslhasdasd', 'url':'images/blair-fraser-410773.jpg'},
    {'title':'Mushroom', 'desc': 'asdlkdslhasdasd', 'url':'images/jaap-straydog-403024.jpg'},
    {'title':'Leaves', 'desc': 'asdlkdslhasdasd', 'url':'images/jeremy-thomas-79493.jpg'},
    {'title':'Lake', 'desc': 'asdlkdslhasdasd', 'url':'images/ricardo-gomez-angel-404673.jpg'},
]

let thumbnails = document.querySelectorAll('.small');

thumbnails.forEach(function(e, i) {
    e.style.backgroundImage = 'url(' + images[i].url + ')';
})

let image = document.querySelector('div.image');
let description = document.querySelector('div.description');

image.addEventListener('mouseenter', function () {
    description.classList.remove('hidden');
});

image.addEventListener('mouseleave', function () {
    description.classList.add('hidden');
});