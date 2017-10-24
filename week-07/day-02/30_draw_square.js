
'use strict';

var lineCount = 6;

// Write a program that draws a
// square like this:
//
//
// %%%%%
// %   %
// %   %
// %   %
// %   %
// %%%%%
//
// The square should have as many lines as lineCount is

console.log('%'.repeat(lineCount));

for (let i = 1; i <= lineCount - 2; i += 1) {
    console.log('%' + ' '.repeat(lineCount - 2) + '%');
}
console.log('%'.repeat(lineCount));