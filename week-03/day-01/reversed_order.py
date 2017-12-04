# Create a method that decrypts reversed-order.txt

def decrypt(file_name):
    with open(file_name) as f:
        lines = list(f.readlines())
    return("".join(lines[::-1]))

print(decrypt("reversed_order.txt"))
