'use strict';

var students = [
        {'name': 'Teodor', 'age': 3, 'candies': 2},
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Zsombor', 'age': 12, 'candies': 5},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Olaf', 'age': 12, 'candies': 7},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
]

// create a function that takes a list of students and logs: 
// - how many candies are owned by students

// create a function that takes a list of students and logs:
// - Sum of the age of people who have lass than 5 candies

function count_candies(studs) {
    let candies = 0;
    for (let i = 0; i < studs.length; i += 1) {
        candies += studs[i]['candies'];
    }
    return candies;
}

function sum_age(studs) {
    let age = 0;
    for (let i = 0; i < studs.length; i += 1) {
        if (studs[i]['candies'] < 5) {
            age += studs[i]['age'];
        }
    }
    return age;
}

console.log(sum_age(students));