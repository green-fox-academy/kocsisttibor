'use strict';
// - Create (dynamically*) a two dimensional list
//   with the following matrix**. Use a loop!
//
//   0 0 0 1
//   0 0 1 0
//   0 1 0 0
//   1 0 0 0
//
// - Print this two dimensional list to the console
//
// * size should depend on a variable
// ** Relax, a matrix is just like an array

var size = 4;

for (let j = 0; j < size; j +=1) {
    console.log('0 '.repeat(size - j - 1) + '1 ' + '0 '.repeat(j))
}