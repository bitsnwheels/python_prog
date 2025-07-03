#author:adarsh raj
# date:5th apr,2023

          #here we are going to study about recursions

# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n*factorial(n-1) 

# print(factorial(5))

           #now we will write a program about fibonacci numbers

def fib(n):
    if(n==0 or n==1):
        return n
    else:
        return (fib(n-1)+fib(n-2))
    
print(fib(9))