'use strict';

var shop_items = ["Cupcake", 2, "Brownie", false]

// Accidentally we added "2" and "false" to the array. 
// Your task is to change from "2" to "Croissant" and change from "false" to "Ice cream"
// No, don't just remove the items :)

shop_items.splice(1, 1, 'Croissant');
shop_items.splice(3, 1, 'Ice cream');
console.log(shop_items);