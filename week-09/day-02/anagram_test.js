const test = require('tape').test;
const anagram = require('./anagram');

test('two empty strings should be true', t => {
    t.true(anagram('', ''));
    t.end();
})

test('two strings with one letter should be true', t => {
    t.true(anagram('a', 'a'));
    t.end();
})

test('two strings with different letter should be false', t => {
    t.false(anagram('a', 'b'));
    t.end();
})

test('two strings with space should be true', t => {
    t.true(anagram('al ma', 'mal a'));
    t.end();
})