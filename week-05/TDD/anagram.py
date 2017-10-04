
def decide_anagram(word1, word2):
    if word1 == '' or word2 == '':
        return False
    elif word1 == None or word2 == None:
        return False 
    text1 =""
    for element in word1:
        if element == " ":
            element = ""
        else:
            text1 += element
    text2 =""
    for element in word2:
        if element == " ":
            element = ""
        else:
            text2 += element
  
    if len(text1) == len(text2) and sorted(text1) == sorted(text2):
        return True
    else:
        return False




