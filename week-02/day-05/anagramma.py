def ask_input():
    words = []
    words.append(input("Please enter first word/phrase:"))
    words.append(input("Please enter second word/phrase:"))
    return(words)


def check(words):
    space_one = words[0].count(" ")
    space_two = words[1].count(" ")
    word_one = list(words[0])
    word_two = list(words[1])
    for i in range(space_one):
        word_one.remove(" ")
    for i in range(space_two):
        word_two.remove(" ")
    word_one.sort()
    word_two.sort()
    if len(word_one) == len(word_two): 
        for letter in range(len(word_one)):
            if word_one[letter] != word_two[letter]:
                return False
                break
    else:
        return False


def anagramma():
    if check(ask_input()) == False:
        print("This is not an anagramma")
    else:
        print("This is an anagramma")

anagramma()
