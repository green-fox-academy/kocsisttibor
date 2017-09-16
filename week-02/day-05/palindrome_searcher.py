# Create a function named search palindrome following your 
# current language's style guide. It should take a string, 
# search for palindromes that at least 3 characters long 
# and return a list with the found palindromes.

given_sting = "dog goat taog"

def checker(characters):
    for i in range(1, int(len(characters) / 2 + 1)):
        if characters[i - 1] != characters[-i]:
            return False
            break
    return True

 
def palindromes(words):
    first_char = 0
    last_char = first_char + 3
    palindromes = []
    while first_char <= len(words) - 3:
        while last_char <= len(words):
            checked_substr = words[first_char:last_char]
            if checker(checked_substr) == True:
                palindromes.append(checked_substr)
                last_char += 1
            else:
                last_char += 1
        first_char += 1
        last_char = first_char + 3
    return palindromes

print(palindromes(given_sting))