'use strict';
// - Create a function called `factorio`
//   that returns it's input's factorial

function factorio(num) {
    let factorio = 1;
    while (num > 1) {
        factorio *= num;
        num -= 1;
    }
    return factorio;
}

console.log(factorio(5));