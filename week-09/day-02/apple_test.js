var test = require('tape').test;
var apple = require('./apples');

test('Apple method should console.log', function(t) {
    var actual = apple();            //the required apple is a function, needs to be executed
    var expected = 'apple';
    t.equal(actual, expected);
    t.end();
})