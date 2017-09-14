# Find part of an integer

# Create a function that takes two strings as a parameter
# Returns the starting index where the second one is starting in the first one
# Returns -1 if the second string is not in the first one
# Example

# input: "this is what I'm searching in", "searching"
# output: 17

def built_in_finder (input_string, output_string):
    return input_string.find(output_string)

# solution without .find()

def is_in (input_string, output_string):
    i = 0
    while i <= len(output_string) - 1:
        part = output_string[:i]
        if part in input_string:
            i += 1
            is_in = True
        else:
            is_in = False
            break
    return is_in

def position (input_string, output_string):
    return(input_string.index(output_string))

def finder (input_string, output_string):
    if is_in(input_string, output_string) == True:  
        return position(input_string, output_string)
    else:
        return -1


print(finder("this is what I'm searching in", "I'm"))