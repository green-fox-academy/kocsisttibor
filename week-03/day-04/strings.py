# Given a string, compute recursively (no loops) a new string where all the
# lowercase 'x' chars have been changed to 'y' chars.

def x_to_y(text):
    if "x" not in text:    # this is not necessary, but makes the function faster :)
        return text
    else:
        if text[0] == "x":
            return "y" + x_to_y(str(text[1:]))
        else:
            return text[0] + x_to_y(str(text[1:]))

print(x_to_y("macskx"))
