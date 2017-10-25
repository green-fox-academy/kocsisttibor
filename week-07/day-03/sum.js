'use strict';
// - Write a function called `sum` that sum all the numbers until the given parameter
// - The function should return the result

var arr = [3, 4, 5, 6];

function sum(arr, limit) {
    let sum = 0;
    for (let i = 0; i <= limit; i += 1) {
        console.log(sum);
        console.log(arr[i]);
        sum += arr[i];
    }
    return sum;
}

console.log(sum(arr, 3));