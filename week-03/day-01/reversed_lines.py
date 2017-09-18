# Create a method that decrypts reversed-lines.txt

def decrypt(file_name):
    with open(file_name) as f:
        content = f.readlines()
    reversed = ""
    for line in content:
        reversed += (line[::-1] + "\n")
    print(reversed)

decrypt("reversed_lines.txt")