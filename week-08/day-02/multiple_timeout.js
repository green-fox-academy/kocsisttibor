'use strict';

// Write a program that prints the following fruits:
// apple -> immediately
// pear -> after 1 seconds
// melon -> after 3 seconds
// grapes -> after 5 seconds

var fruits = ['grapes', 'melon', 'pear', 'apple']
var times = [5000, 5000, 3000, 1000]

function printer() {
    console.log(fruits.pop())
}

for (let i = 0; i < fruits.length; i += 1) {
    setTimeout(printer, times[fruits.length - i])
}