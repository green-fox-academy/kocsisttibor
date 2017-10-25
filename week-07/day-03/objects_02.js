'use strict';

var students = [
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Zsombor', 'age': 12, 'candies': 5}
]

// create a function that takes a list of students and logs:
// - Who has got more candies than 4 candies

// create a function that takes a list of students and logs: 
//  - how many candies they have on average

function who_has_more(studs) {
    let luckies = [];
    for (let i = 0; i < studs.length; i += 1) {
        if (studs[i]['candies'] > 4) {
            luckies.push(studs[i]['name']);
        }
    }
    return luckies;
}

function count_candies(studs) {
    let candies = 0;
    for (let i = 0; i < studs.length; i += 1) {
        candies += studs[i]['candies'];
    }
    return candies;
}

function average(studs) {
    return count_candies(studs) / studs.length;
}
