# author:adarsh raj
# date:1st apr,2023

def add(a=2,b=4,c=6):
    return a+b+c

def average(*numbers):    #with the help of this we can pass varible length arguements
    sum=0    
    for i in numbers:
        sum=sum+i
    print("average is ",sum/len(numbers))


# result=add(12,12,5)
# print(result)   #will print 29


# result=add()
# print(result)   #will print 12

# result=add(1)
# print(result)   #will print 11

# result=add(1,2)
# print(result)   #will print 9



                                       #in python we can also do this


result=add(c=1,a=2,b=9)   #here,we are writing the variable names itself.also we are able to change the order in which the parameters are passed
print(result)   #will print 12

average(2,5,6)