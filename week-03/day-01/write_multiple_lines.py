# Create a function that takes 3 parameters: a path, a word and a number,
# than it should write to a file.
# The path parameter should be a string, that describes the location of the file.
# The word parameter should be a string, that will be written to the file as lines
# The number paramter should describe how many lines the file should have.
# So if the word is "apple" and the number is 5, than it should write 5 lines
# to the file and each line should be "apple"
# The function should not raise any error if it could not write the file.

def multiple_word_writer(path, word, number):
    with open(path, "w") as f:
        f.write((word + "\n") * number )

multiple_word_writer("C:\E\GreenFox\kocsisttibor\week-03\day-01\multiple_lines.txt", "apple", 5)