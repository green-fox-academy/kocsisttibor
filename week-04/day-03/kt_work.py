# https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/testing/apples/python.md
# https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/testing/sum/python.md
# https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/testing/anagram/anagram.md

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
