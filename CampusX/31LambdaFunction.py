# lambda input:expression
# lambda function has no return value
# can only be written in one line
# lambda function are not exactly used for code reusabitliy. 
# no name of lambda function
# used along with higher order function. Higher order function
# are functions which need any other function as an input
# or the functions which are returning any other function


# a lambda function to return the square of a number
f =lambda x:x**2
print(f(9))

a=lambda x,y:x+y
print(type(a))
print(a(4,5))


a = lambda s:s[0]=='a'
print(a("apple"))
print(a("bapple"))

b = lambda x:"Even " if x%2==0 else "odd"
print(b(3))
print(b(4))

# higher order functions
def return_sum(func,L):
    result = 0
    
    for i in L:
        if func(i):
            result += i
    return result

x = lambda x:x%2==0
y = lambda x: x%2==1
z = lambda x:x%3==0

L=[3,5,1,2,6,8,4]
print(return_sum(x,L))
print(return_sum(y,L))
print(return_sum(z,L))


#inbuilt lambda functions
#Map
#Filter
#Reduce

# L=[1,2,3,4,5,6,7]
# # when we pass a lambda function and an iterable then we can apply that lambda function
# # on which element of that iterable
# print(map(lambda x:x*2,L))
# print(list(map(lambda x:x*2,L)))
# print(list(map(lambda x:x%2==0,L)))


# filter filters the elmeents of an iterable based on a given condtion
# unlike map which applies that lambda fucntion on each of the element
# L=[1,2,3,4,5,6,7]
# print(list(filter(lambda x:x>4,L)))



# Now we are going to see the application of reduce. It comes under the functools library
# at each iteration it takes the first two operands and then does the required
# operations at those. This ultimately reduces the list to a single digit
# import functools
# L=[1,2,3,45 ,5,6,7]
# print(functools.reduce(lambda x,y:x+y, L))  
# print(functools.reduce(lambda x,y:x if x>y else y,L)) # this functionwill print the largest elment in the lsit


# List Comprehension
l = [1,2,3,4,5,6,7]
l1 = [item*2 for item in l]
print(l1)
l2 = [i**2 for i in range(10)]
print(l2)

l3 = [i**2 for i in range(10) if i%2==1]
print(l3)

# dictionary comprehension

D={"Name":"Adarsh","Gender":"Male,","Age":30}
print(D.items())

d1 = {key:value for key,value in D.items() if len(key) > 3}