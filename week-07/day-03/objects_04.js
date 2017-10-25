'use strict';

var watchlist = []

var security_alchol_loot = 0

var queue = [
	{ 'name': 'Amanda', 'alcohol': 10, 'guns': 1 },
	{ 'name': 'Tibi', 'alcohol': 0, 'guns': 0 },
	{ 'name': 'Dolores', 'alcohol': 0, 'guns': 1 },
	{ 'name': 'Wade', 'alcohol': 1, 'guns': 1 },
	{ 'name': 'Anna', 'alcohol': 10, 'guns': 0 },
	{ 'name': 'Rob', 'alcohol': 2, 'guns': 0 },
	{ 'name': 'Joerg', 'alcohol': 20, 'guns': 0 }
]

// Queue of festivalgoers at entry
// no. of alcohol units 
// no. of guns

// Create a security_check function that returns a list of festivalgoers who can enter the festival

// If guns are found, remove them and put them on the watchlist (only the names)
// If alcohol is found confiscate it (set it to zero and add it to security_alchol_loot) and let them enter the festival

function check_in(queue) {
    let festivalgoers = [];
    let watchlist = []
    let alcohol_loot = 0;
    for (let i = 0; i < queue.length; i += 1) {
        if (queue[i].guns === 0) {
            festivalgoers.push(queue[i].name);
            alcohol_loot += queue[i].alcohol;
        } else {
            watchlist.push(queue[i].name)
        }
    }
    return festivalgoers;
}
