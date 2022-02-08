#!/usr/bin/env python3

height = int(input("How tall are you? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("what is your age? "))
    if age < 12:
        print("Child tickets are $5.")
        bill = 5
    elif age <= 18:
        print("Youth tickets are $7.")
        bill = 7
    else:
        print("Adult tickets are $12.")
        bill = 12

    wants_photo = input("Do you want a picture taken? Y or N. ")

    if wants_photo == "Y":
        #add $3 to the bill
        print("Pictures are an additional $3.")
        bill += 3
        # above is equivalent to bill = bill + 3
        # note, there is no else action here, so you can leave off the `else`
    print(f"Your final bill is {bill}.")
                        
else:
    print("Sorry, you have to grow taller before you can ride.")
