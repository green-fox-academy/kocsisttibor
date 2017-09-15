user_input = list(input("Enter a word or phrase: "))

def create_palindrome(phrase):
    palindrome = []
    for char in range(len(phrase)):
        palindrome.append(phrase[-char-1])
    palindrome = phrase + palindrome
    print("".join(palindrome))

create_palindrome(user_input)