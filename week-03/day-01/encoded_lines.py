# Create a method that decrypts encoded-lines.txt

abc = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ[  / " (,--.*+'
abc_list = list(abc)


def decrypt(file_name):
    with open(file_name) as f:
        content = list(f.read())
    for i in range(len(content)):
        if content[i] == " ":
            content[i] = " "
        elif content[i] != "\n":
            content[i] = abc_list[int(abc_list.index(content[i])) - 1]
    print("".join(content))

decrypt("encoded_lines.txt")