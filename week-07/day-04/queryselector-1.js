// 1
var king = document.querySelector('#b325');

// 2
var conceited = document.querySelector('.asteroid.b326');

// window.alert(conceited);

// 3
var businessLamp = document.querySelectorAll('.big');

businessLamp.forEach(function(x) {
    console.log(x);
});

// 4
var firstSection = document.body.getElementsByTagName('section');
var conceitedKing = firstSection[0].getElementsByTagName('div');

// window.alert(conceitedKing[0]);
// window.alert(conceitedKing[1]);

// option #2
// conceitedKing = document.querySelectorAll('.container .asteroid')

// 5
var noBusiness = document.getElementsByTagName('div');
noBusiness = Array.from(noBusiness);

noBusiness.forEach(function(x) {
    window.alert(x);
});

// 6
var allBizniss = document.querySelectorAll('.asteroid.big');

// window.alert(allBizniss);