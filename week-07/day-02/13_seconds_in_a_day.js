
'use strict';

var currentHours = 14;
var currentMinutes = 34;
var currentSeconds = 42;

// Write a program that prints the remaining seconds (as an integer) from a
// day if the current time is represented by these variables
let remaining_seconds = 60 - currentSeconds + 60 * (60 - (currentMinutes - 1)) + 3600 * (24 - (currentHours - 1))
console.log('Remaining seconds: ' + remaining_seconds);