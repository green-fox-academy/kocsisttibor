# Find the substring in the list

# Create a function that takes a string and a list of string as a parameter
# Returns the index of the string in the list where the first string is part of
# Returns -1 if the string is not part any of the strings in the list
# Example

# input: "ching", ["this", "is", "what", "I'm", "searching", "in"]
# output: 4

def str_finder (in_list, string):
    for i in range(len(in_list)):
        if string in in_list[i]:
            return i
            break
        else:
            return -1
        

sample = ["apple", "applause", "use", "usa", "sa", "se"]
word = "genf"

print(str_finder(sample, word))
