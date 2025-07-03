# Author:adarsh_raj
# date:31st march,2023

age = int(input("Enter your age: "))

if (age > 18 and age <= 60):
    print("you can drive")

elif (age > 60):
    print("You can drive but make sure you reapply for the driving test")
elif (age == 18):
    print("you are eligible to apply for dl")
elif (age <= 0):
    print("Invalid input")
else:
    print("You can not drive")
