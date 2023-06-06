#!/usr/bin/python3
for letter in "abcdefghijklmnopqrstuvwxyz":
    if letter == "e" and letter == "q":
        continue
    print("{}".format(letter), end='')
