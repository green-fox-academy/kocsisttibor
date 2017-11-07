var test = require('tape').test;
var sums = require('./sum');

test('sums method should sum 3 number elements', function(t) {
    var actual = sums([5, 4, 8]);
    var expected = 17;
    t.equal(actual, expected);
    t.end();
})

test('sums method should sum empty list elements', function(t) {
    var actual = sums([]);
    var expected = 0;
    t.equal(actual, expected);
    t.end();
})

test('sums method should sum one-element list elements', function(t) {
    var actual = sums([5]);
    var expected = 5;
    t.equal(actual, expected);
    t.end();
})

test('sums method should sum one-element list elements', function(t) {
    try{
        sums(null);
    } catch (e) {
        t.error(e, "null test")
    }
    t.end();
}) // it doesn't work, who knows why