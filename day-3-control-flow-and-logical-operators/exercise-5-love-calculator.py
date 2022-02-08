#!/usr/bin/env python3

# BEGIN project code
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# END project code

# concat the names together
name_pair = name1 + name2

# count for the letters of true in both names
true_count = (
        name_pair.lower().count("t") 
        + name_pair.lower().count("r") 
        + name_pair.lower().count("u") 
        + name_pair.lower().count("e")
)

# count for the letters of true in both names
love_count = (
        name_pair.lower().count("l") 
        + name_pair.lower().count("o") 
        + name_pair.lower().count("v") 
        + name_pair.lower().count("e")
)

# concat numbers together and convert back to an int to remove leading zeroes
compatibility = int(str(true_count) + str(love_count))

print(f"You are {compatibility}% compatible.")
