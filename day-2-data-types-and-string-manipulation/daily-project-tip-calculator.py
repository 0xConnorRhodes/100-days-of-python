#!/usr/bin/env python3

print("Welcome to the Tip Calculator")

bill_amt = float(input("What was the total bill? $"))

tip_pct = 100 / float(input("What percentage tip would you like to give? "))

split_amt = int(input("How many people will split the bill? "))

individual_amt = bill_amt * tip_pct / split_amt

print(f"Each person should pay ${individual_amt}")
