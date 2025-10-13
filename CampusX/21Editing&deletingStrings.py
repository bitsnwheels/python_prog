c = "hello"

#strings are immutable data type as a result
#the below line will not execute
# c[0]='X' #throws error

c="world"  #this is valid

#c[5]='x' #even this is not allowed 
print(c)

# del c[0] #not allowed
del c #allowed
# print(c) # will throw error as c no longer exists