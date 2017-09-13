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
