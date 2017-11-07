'use strict';

// Handle the exceptions in the addString() function. It should check the type of the
// arguments, throw the right error and write it to the console.
// It should add the strings too if the arguments are appropriate.

let printStr = function(str) {
  console.log(str);
}

let  addString = function(str1, str2, printStr){
  let newStr = str1 + str2;
  printStr(newStr);
}

try {
    addString(1234, 56789, 'printStr');
} catch (e) {
    if (e instanceof TypeError) {
        console.log('All parameters need to be string')
    }
}