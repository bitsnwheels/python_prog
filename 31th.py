# author:adarsh raj
# date:12th apr,2023


a=input("enter the number: ")

"""
here if we dont use the try except method then the code which is below the code for
multiplication table wont run if we give an invalid input to a.In order to avoid it 
we have used try except method which will let the codes below it run even if an invalid
input is given
"""
try:
    for i in range(1,11):
     print(f"{int(a)} X {int(i)}={int(a)*int(i)}")
except Exception as e:
    print(e)
    
print("some important lines of code")
print("End of the program")

#we can also raise a particular type of error like vlaue error or index error etc:
try:
    a=int(input("Enter an integer")) #if any input other than integer is given then value error will be triggered
    s=[3,5]
    print(s[a]) #if an incorrect index is provided then indexerror will be trigerred

except ValueError:
    print("Number entered is not an integer")
except IndexError:
    print("Invalid index")