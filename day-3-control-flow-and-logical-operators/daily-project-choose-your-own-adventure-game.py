#!/usr/bin/env python3

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.")

choice1 = input('You\'re at a cross road. Where would you like to go? Type "left" or "right" ').lower()


if choice1 == "right":
    print("You got lost and died of dysentery.")
    exit()
else:
    choice2 = input('You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. ').lower()

if choice2 == "swim":
    print("You have drowned and died of dysentery.")
    exit()
else:
    choice3 = input('The boat takes you across the lake to a house. Inside the house there are three doors. Choose which door to open. Type "red", "blue", or "yellow." ').lower()

if choice3 == "red":
    print("Behind the door is a monster which holds you prisoner until you die of dysentery.")
    exit()
elif choice3 == "blue":
    print("Behind the door is a bottomless pit which you fall into. You fall continuously until you die of dysentery.")
    exit()
else:
    print("You have won.")
    exit()



