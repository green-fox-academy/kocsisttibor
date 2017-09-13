accounts = [
	{ 'client_name': 'Igor', 'account_number': 11234543, 'balance': 203004099.2 },
	{ 'client_name': 'Vladimir', 'account_number': 43546731, 'balance': 5204100071.23 },
	{ 'client_name': 'Sergei', 'account_number': 23456311, 'balance': 1353600.0 }
]

# Create function that returns the name and balance of cash on an account

# Create function that transfers an amount of cash from one account to another
# it should have three parameters:
#  - from account_number
#  - to account_number
#  - amount to transfer
#
# Print "404 - account not found" if any of the account numbers don't exist

def name_and_balance(acc_num):
    name_and_balance = []

    for i in range(len(accounts)):
        if accounts[i]["account_number"] == acc_num:
            name_and_balance.append(accounts[i]["client_name"])
            name_and_balance.append(accounts[i]["balance"])

    return name_and_balance

print(name_and_balance(43546731))

def transfer(from_account, to_account, value):
    account_numbers = []
    for i in range(len(accounts)):
        account_numbers.append(accounts[i]["account_number"])
    for i in range(len(accounts)):
        if from_account not in account_numbers or to_account not in account_numbers:
            print("404 - account not found")
            break
        if accounts[i]["account_number"] == from_account:
            accounts[i]["balance"] -= value
        elif accounts[i]["account_number"] == to_account:
            accounts[i]["balance"] += value
    return accounts

print(transfer(11234542, 23456311, 4099))



