
'use strict';
// - Create a function called `printer`
//   which logs to the console the input parameters
//   (can have multiple number of arguments)


function printer() {
    for (let i = 0; i < arguments.length; i += 1) {
        console.log(arguments[i]); 
    }
}

printer('apple pear', 5)