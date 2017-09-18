# Write a function that copies a file to an other
# It should take the filenames as parameters
# It should return a boolean that shows if the copy was successful

def copy_file(file1, file2):
    try:
        with open(file1, "r") as f:
            content = f.read()
        with open(file2, "w") as f:
            f.write(content)
        print("OK!")
    except:
        print("Not OK!")

source = "C:\E\GreenFox\kocsisttibor\week-03\day-01\multiple_lines.txt"
goal = "C:\E\GreenFox\kocsisttibor\week-03\day-01\copied_content.txt"

copy_file(source, goal)
