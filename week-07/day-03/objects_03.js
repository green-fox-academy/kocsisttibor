'use strict';

var accounts = [
	{ 'client_name': 'Igor', 'account_number': 11234543, 'balance': 203004099.2 },
	{ 'client_name': 'Vladimir', 'account_number': 43546731, 'balance': 5204100071.23 },
	{ 'client_name': 'Sergei', 'account_number': 23456311, 'balance': 1353600.0 }
]

// Create function that returns the name and balance of cash on an account

// Create function that transfers an amount of cash from one account to another
// it should have three parameters:
//  - from account_number
//  - to account_number
//  - amount of cash to transfer
//
// Log "404 - account not found" if any of the account numbers don't exist to the console.

function is_valid(account) {
    let account_numbers = []
    for ( let i = 0; i < accounts.length; i += 1) {
        account_numbers.push(accounts[i].account_number);
    }
    return account_numbers.includes(account)
}

function give_details(account) {
    if (is_valid(account) === false) {
        console.log('404 - account not found');
    } else {
        let name = '';
        let balance = 0;
        for ( let i = 0; i < accounts.length; i += 1) {
            if (accounts[i].account_number === account) {
                name = accounts[i].client_name;
                balance = accounts[i].balance;
                console.log('client name: ' + name);
                console.log('balance: ' + balance);
            }
        }
    }
}

function transfer(from, to, amount) {
    for ( let i = 0; i < accounts.length; i += 1) {
        if (accounts[i].account_number === from) {
            accounts[i].balance -= amount;
        }
        if (accounts[i].account_number === to) {
            accounts[i].balance += amount;
        }
    }
}

transfer(23456311, 43546731, 3600);
console.log(accounts);
