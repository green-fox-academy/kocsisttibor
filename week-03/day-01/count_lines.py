# Write a function that takes a filename as string,
# then returns the number of lines the file contains.
# It should return zero if it can't open the file, and
# should not raise any error.

filename = input("Enter a filename: ")

def count_lines(filename):
    try:
        with open(filename, "r") as f:
            lines = 0
            for line in f:
                lines += 1
        return lines
    except FileNotFoundError:
        return 0


print(count_lines(filename))