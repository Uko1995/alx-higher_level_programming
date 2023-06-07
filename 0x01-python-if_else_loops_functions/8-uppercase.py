#!/usr/bin/python3
def uppercase(str):
    for character in str:
        uppercase = chr(ord(character) - 32) if 97 <= ord(character) <= 122 else character
        print("{}".format(uppercase), end="")
    
    print()
