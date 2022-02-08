#!/usr/bin/env python3

height = int(input("How tall are you? "))

# modify the code so those 45-55 ride for free

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("what is your age? "))
    if age < 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    if age >= 45 and age <= 55:
        print("You get to ride for free.")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you have to grow taller before you can ride.")

