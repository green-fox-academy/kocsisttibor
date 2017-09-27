# https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/testing/apples/python.md
# https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/testing/sum/python.md
# https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/testing/anagram/anagram.md
# https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/testing/count-letters/count-letters.md

class Apple(object):

    def get_apple(self):
        return "apple"

class Sum(object):

    def sum_of_numbers(self, list_of_ints=None):
        if list_of_ints == None:
            return None
        else:
            return sum(list_of_ints)

class Anagramma(object):

    def anagramma(self, string_1, string_2):
        if len(string_1) != len(string_2):
            return False
        else:
            return sorted(string_1) == sorted(string_2)

class CountLetter(object):

    def count_letter(self, string_1):
        letters = {}
        for i in string_1:
            if i in letters.keys():
                letters[i] += 1
            else:
                letters[i] = 1
        return letters
