# Create a method that decrypts the duplicated-chars.txt

def decrypt(file_name):
    with open(file_name) as f:
        content = f.read()
    print(content)
    decrypted = content[3:int(len(content)):2]
    print(decrypted)
     
decrypt("duplicated-chars.txt")