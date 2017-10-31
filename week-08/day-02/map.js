'use strict';

var fruits = [
  'melon',
  'apple',
  'strawberry',
  'blueberry',
  'pear',
  'banana'
];

// Create a new array of consists numbers that shows how many times the 'e' letter
// occurs in the word stored under the same index at the fruits array!
// Please use the map method.

var listWithLetters = fruits.map(function(x) {
    var eNums = x.split('').filter(function(y) {
        if (y === 'e') {
            return 1;
        }
    })
    return eNums.length
});

console.log(listWithLetters)

var nums = [3, 4, 5]

console.log(nums.s)