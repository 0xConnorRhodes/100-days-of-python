#!/usr/bin/env python3

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

# NOTE: for each item in list, set var to += the list and then divide var by the number of items in the list


total_height = 0

for height in student_heights:
    total_height += height

print(total_height)

#number_of_students len(student_heights)

#avg_height = total_heights / number_of_students

#print(avg_height)
