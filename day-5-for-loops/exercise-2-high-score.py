#!/usr/bin/env python3

# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

list_items = len(student_scores)

# NOTE:for each number of item in the list, check if it is greater than other numbers
for n in range (0, len(student_scores)):
    item_to_check = student_scores[n]
    print(item_to_check)


#print(list_items)

#for item in student_scores:


#print(f"The highest score in the class is: {high_score}")
