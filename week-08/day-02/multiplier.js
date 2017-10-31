

// Create the multiplier function that you can use like this:
'use strict'

function multiplier(x) {
    return function(y) {
        return x * y;
    }
}

const duplicator = multiplier(2); //calling the multiplier with parameter 2 the x is set to 2; the multiplier returns the inner function which awaits for another parameter (y), this is set when duplicator is called; finally the inner function returns the multiply

console.log(duplicator(5)); // should log 10
console.log(duplicator(10)); // should log 20

const threeTimes = multiplier(3);

console.log(threeTimes(5)); // should log 15
console.log(threeTimes(100)); // should log 300