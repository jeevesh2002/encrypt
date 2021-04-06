import os
import decrypt
import encrypt
key1=13
key2=int(input("enter key"))

choice = (input("enter encrypt or decrypt"))
path = input(r'Enter path of Image directory : ')
for subdir, dirs, files in os.walk(path):
    for filename in files:
        filepath = subdir + os.sep + filename
        if choice == "encrypt":
            if filepath.endswith(".jpg") or filepath.endswith(".png") or filepath.endswith(".jpeg"):
                encrypt.encrypt(filepath,key1)
        elif choice == "decrypt" and key2 == key1:
            if filepath.endswith(".jpg") or filepath.endswith(".png") or filepath.endswith(".jpeg"):
                decrypt.decrypt(filepath,key2)
        else :
            pass
