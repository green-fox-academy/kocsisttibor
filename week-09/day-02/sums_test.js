var test = require('tape').test;
var sums = require('./sum');

var listOfNumbers = [5, 4, 8];

test('sums method should sum all elements', function(t) {
    var actual = sums(listOfNumbers);
    var expected = 17;
    t.equal(actual, expected);
    t.end();
})