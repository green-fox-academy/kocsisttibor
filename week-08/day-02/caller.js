'use strict';

// Implement the selectLastEvenNumber function that takes an array and callback,
// it should call the callback immediately with the last even number on the array


function printNumber(num) {
  console.log(num);
}

function selectLastEvenNumber(listOfNumbers, callback) {
    let evens = listOfNumbers.filter(function(x) {
        return x % 2 === 0
    })
    console.log(evens)
    callback(evens[evens.length - 1])
}

selectLastEvenNumber([2, 5, 7, 8, 9, 11], printNumber); // should print 8