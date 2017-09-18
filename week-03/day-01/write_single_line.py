# Open a file called "my-file.txt"
# Write your name in it as a single line
# If the program is unable to write the file,
# then it should print an error message like: "Unable to write file: my-file.txt"

def name_writer():
    try:
        with open("my-file2.txt", "w") as f:
            f.write("Tibi")
    except Exception as e:
        print("Unable to write file: " + e.filename)

        
name_writer()