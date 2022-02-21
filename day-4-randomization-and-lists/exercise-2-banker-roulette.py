#!/usr/bin/env python3

import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

number_of_people = len(names)

# Here was my first off by one error.
winner = names[random.randint(0, number_of_people - 1)]

print(f"{winner} is going to buy the meal today!")

