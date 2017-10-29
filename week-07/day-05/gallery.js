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
let desc_title = document.querySelector('h3.description');
let desc_par = document.querySelector('p.description');
let image_index = 0;

function image_setter() {
    image.style.backgroundImage = 'url(' + images[image_index].url + ')';
    desc_title.textContent = images[image_index].title;
    desc_par.textContent = images[image_index].desc;
}

image_setter();

image.addEventListener('mouseenter', function () {
    description.classList.remove('hidden');
});

image.addEventListener('mouseleave', function () {
    description.classList.add('hidden');
});

thumbnails.forEach(function(e, i) {
    e.addEventListener('mouseenter', function() {
        e.classList.add('before_select')
    });
    e.addEventListener('mouseleave', function() {
        e.classList.remove('before_select')
    });  
});

let side = document.querySelectorAll('.side');

side.forEach(function(e){
    e.addEventListener('mouseenter', function () {
        e.classList.add('button_hover');
    });
    
    e.addEventListener('mouseleave', function () {
        e.classList.remove('button_hover');
    });
})

let left_side = document.querySelector('.left.side')
let right_side = document.querySelector('.right.side')

left_side.addEventListener('click', function() {
    image_index -= 1;
    image_setter();
    right_side.classList.remove('inactive')
    if (image_index === 0) {
        left_side.classList.add('inactive')
    }
})

right_side.addEventListener('click', function() {
    image_index += 1;
    image_setter();
    left_side.classList.remove('inactive')
    if (image_index === images.length) {
        right_side.classList.add('inactive')
    }
})