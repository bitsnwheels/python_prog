# Author:Adarsh Raj
# date:31st march,2023

# match case statements are similar to switch case statements.the only difference
# is in case of former we used to have break statements but in this case we dont need this
#   also we can than one default cases in this case
#  also we can have conditionhave more s in the default case

x = int(input("enter the value of x: "))

match x:
    case 0:
        print("x is zero")
    case 4:
        print("x is four")
    case _ if x > 90:
        print("x is greater than ninety")
    case _:  # this is default case
        print(x)
