'use strict';
// - Create a variable named `aj`
//   with the following content: `[3, 4, 5, 6, 7]`
// - Reverse the order of the elements in `aj`
// 		- do it with the built in method
//		- do it with creating a new temp array and a loop
// - Print the elements of the reversed `aj`

var aj = [3, 4, 5, 6, 7];

console.log(aj.reverse());

var new_array = [];
for (let i = 0; i < aj.length; i += 1) {
    new_array.unshift(aj[i]);
}

console.log(new_array);