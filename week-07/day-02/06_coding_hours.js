'use strict';

// An average Green Fox attendee codes 6 hours daily
// The semester is 17 weeks long
//
// Print how many hours is spent with coding in a semester by an attendee,
// if the attendee only codes on workdays.
//
// Print the percentage of the coding hours in the semester if the average
// work hours weekly is 52

let daily_hours = 6;
let weeks = 17;
let coding_hours = daily_hours * 5 * weeks

console.log('Coding hours in a semester: ' + coding_hours);
console.log('Precentage: ' + coding_hours * 100 / (52 * weeks));