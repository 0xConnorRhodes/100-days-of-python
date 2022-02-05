#/usr/bin/env python3

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

BMI = round(weight / height ** 2)

if BMI < 18.5:
    BMI_interpretation = "you are underweight."
else: BMI_interpretation = "you are clinically obese."

print(f"Your BMI is {BMI}, you are {BMI_interpretation}")
