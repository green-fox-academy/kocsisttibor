# This should be a simple word counter which give us the most common word in a file
# If ran from the command line without arguments it should print out the usage:
# python most_common_word.py [source]
# When the argument provided and the source is a file
# count all words in the given file and print the most common 
# ("cat", "CAT", "cat," "cat." are different words ) 

import sys

def get_arguments():
    return sys.argv


def read_from_file(filename):
    with open(filename) as f:
        return f.read()


def most_common_word(filename):
    words_list = read_from_file(filename).split()
    most_common = None
    occurrence = 0
    for word in words_list:
        if words_list.count(word) >= occurrence:
            most_common = word
            occurrence = words_list.count(word)
    return most_common


def controller():
    arguments = get_arguments()
    if len(arguments) == 1:
        print("Usage:\npython most_common_word.py [source]")
    elif len(arguments) == 2: #and arguments[1][-4:] == ".txt":
        print("Most common word: " + most_common_word(arguments[1]))
    else:
        print("Usage:\npython most_common_word.py [source]")

controller()