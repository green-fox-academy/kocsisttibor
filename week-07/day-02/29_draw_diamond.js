'use strict';

var lineCount = 7;



// Write a program that draws a
// diamond like this:
//
//
//    *
//   ***
//  *****
// *******
//  *****
//   ***
//    *
//
// The diamond should have as many lines as lineCount is

if (lineCount % 2 === 0) {
    for (let i = 1; i <= lineCount / 2; i += 1) {
        console.log(' '.repeat(lineCount / 2 - i) + '*'.repeat(2 * i - 1));
    }
    for (let i = lineCount / 2; i > 0; i -= 1) {
        console.log(' '.repeat(lineCount / 2 - i) + '*'.repeat(2 * i -1));
    }
} else {
    for (let i = 1; i <= lineCount / 2 + 1; i += 1) {
        console.log(' '.repeat(lineCount / 2 + 1 - i) + '*'.repeat(2 * i - 1));
    }
    for (let i = lineCount / 2 - 1; i > 0; i -= 1) {
        console.log(' '.repeat(lineCount / 2 - i) + '*'.repeat(2 * i));
    }
}