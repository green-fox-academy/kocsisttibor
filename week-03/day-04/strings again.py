
# Given a string, compute recursively a new string where all the 'x' chars have been removed.

def x_to_y(text):
    if "x" not in text:   
        return text
    else:
        if text[0] == "x":
            return x_to_y(str(text[1:]))
        else:
            return text[0] + x_to_y(str(text[1:]))

print(x_to_y("fexlix"))