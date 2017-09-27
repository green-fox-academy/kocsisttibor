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

    def ask_input(self):
        self.words = []
        self.words.append(input("Please enter first word/phrase:"))
        self.words.append(input("Please enter second word/phrase:"))
        return(self.words)


    def check(self, words):
        space_one = self.words[0].count(" ")
        space_two = self.words[1].count(" ")
        word_one = list(self.words[0])
        word_two = list(self.words[1])
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


    def anagramma(self):
        return self.check(self.ask_input()) != False

