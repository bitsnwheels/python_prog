def is_even(n):
    """
    This function takes an integer as an input and returns if it is an even number
    Input- Any valid Integer
    Output- odd/even
    Created By - Adarsh
    Last Edited: 11 oct 2025
    """
    if(type(n)==int):
        if n%2==0:
            return "Even"
        else:
            return "Odd"
    else:
        return "Input of incorrect format"


# for i in range(1,11):
#     print(is_even(i))   
# print(is_even("adfsd"))

# print(is_even.__doc__) 

# def power(a=1,b=1):
#     return a**b

# print(power()) # default arguements
# print(power(2)) # default arguements
# print(power(2,3))  # this is an example of positional arguement
# print(power(b=3,a=2)) # this is an example of keyword arguement. Keyword arguement overwrites positional arguements



# an example of arbitrary arguement based funcition. Here the number
# of inputs is not known beforehand and as a result , we use this 
# syntax of arbitrary arguements. Here parameter "arguement" is a tuple
def flexiMultiplier(*number):  
    # print(number)
    # print(type(number))  # will print tuple
    product = 1
    for i in number:
        product = product * i
    return product

# print(flexiMultiplier(3,3))
# print(flexiMultiplier(3))
# print(flexiMultiplier(3,2,4,1))  
# print(flexiMultiplier(3,6,2,6,3))


# Here the function can use the global varible as it is not trying to 
# change its value
# def h(y):
#     print(x)
#     print(x+1)
    
# x= 5
# h(x)
# print(x)



# Here the function can't use the global varible as it is trying to 
# change the global variable
# def h(y):
#     x+=1  #will throw an error
#     print(x+1)
    
# x= 5
# h(x)
# print(x)


# With the help of this approach we can do changes with global varialbe
# inside a function but it is not a good practice and we should avoid
# it as much as possible.
# def h(y):
#     global x
#     x+=1  #will not  throw an error
#     print(x+1)
    
# x= 5
# h(x)
# print(x)


# in python , functions behave exactly same as int ,,stirng ,orn any other data tyepe
# becuase ultimately everything is pytthon is an object
def f(num):
    return num**2

l = [1,3,1,f]
print(l[-1](3))  










