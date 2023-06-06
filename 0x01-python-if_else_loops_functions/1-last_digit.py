#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_digit = (abs(number) % 10) * -1
    end_str = "and is less than 6 and not 0"
    print(f"Last digit of {number} is {last_digit} {end_str}")
if number > 0:
    last_digit = number % 10
    end_str = "and is greater than 5"
    if last_digit > 5:
        print(f"Last digit of {number} is {last_digit} {end_str}")
    elif last_digit == 0:
        print(f"Last digit of {number} is {last_digit} and is 0")
    elif last_digit < 6 and last_digit > 0:
        end_str2 = "and is less than 6 and not 0"
        print(f"Last digit of {number} is {last_digit} {end_str2}")
