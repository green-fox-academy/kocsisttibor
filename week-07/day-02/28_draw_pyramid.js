'use strict';

var lineCount = 4;

// Write a program that draws a
// pyramid like this:
//
//
//    *
//   ***
//  *****
// *******
//
// The pyramid should have as many lines as lineCount is

for (let i = 1; i <= lineCount; i += 1) {
    console.log(' '.repeat(lineCount - i) + '*'.repeat(2 * i - 1) );
} 