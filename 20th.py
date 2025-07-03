# author:adarsh raj
# date:2nd apr,2023

#tuples are verys much similar to lists except the fact that lists are mutable and tuples are not!

tup=(1,2,4,6,3)
print(tup)

# note: all the functionalities of lists are valid in tuples also like slicing,negative indexing etc

if 6 in tup:
    print("yes")

print(len(tup))

# note: a tuple with a single element without comma will be treated as an int but with a comma it will treated like a tuple as shown below:
tup1=(1)
tup2=(1,)
print(type(tup1))   #it will print int
print(type(tup))      #it will print tuple