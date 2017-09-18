# Create a method that decrypts reversed-order.txt

def decrypt(file_name):
    with open(file_name) as f:
        lines = list(f.readlines())
    line = len(lines) - 1
    decrypted = []
    while line >= 0:
        decrypted.append(lines[line])
        line -= 1
    return("".join(decrypted))

print(decrypt("reversed_order.txt"))
