let arr = [1 , 23, 45, 6, 8, 2];
console.log(arr.length);
arr.length = 3;
console.log(arr)

let arr2 = new Array(4).join('apple')
console.log(arr2)

arr.forEach(function(item) {
    console.log(item + 2);
});

arr.forEach(console.log(item + 2))