#!/usr/bin/env python3

print("Welcome to the Tip Calculator")

bill_amt = float(input("What was the total bill? $"))

tip_pct = float(input("What percentage tip would you like to give? ")) / 100

split_amt = int(input("How many people will split the bill? "))

total_amt = round(bill_amt + (bill_amt * tip_pct), 2)
rounded_total_amt = "{:.2f}".format(bill_amt + (bill_amt * tip_pct), 2)

#individual_amt = round(total_amt / split_amt, 2)
individual_amt = "{:.2f}".format(total_amt / split_amt, 2)

print(f"The total amount is ${rounded_total_amt}.")

print(f"Each person should pay ${individual_amt}.")


# optional more condensed answer, written for a challenge
#answer = round((bill_amt + (bill_amt * tip_pct)) / split_amt, 2)

#print(f"Each person should pay ${answer}.")
