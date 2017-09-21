
# Given a string, compute recursively a new string where all the
# adjacent chars are now separated by a "*".

def chars_and_stars(text):
    if len(text) == 1:
        return text
    elif len(text) == 2:
        return chars_and_stars(text[0]) + "*" + text[1]
    else:
        return text[0] + "*" + chars_and_stars(str(text[1:]))

print(chars_and_stars("abc"))