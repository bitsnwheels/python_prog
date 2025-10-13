# sets do not allow duplicates
# sets dont have indexing or slicing
# sets dont allow mutable data types e.g. list
# sets itself is  a mutable data type. This means 2d sets are notpossible

s = {} #this is by default a dictinoary
print(type(s)) 

s1 = set()

s1 = {1,2,3,4,5}
s2 = {"Hlloe",2,4.5,True}

# s3 = {1,1,1,2,2,3}
# print(s3) # only unique elemensts will be printed

# s4 = {1,2,[1,341,1]} #throws error as list is a mutable data type and sets dont allow mutable data teype


#everytime you print the below lines then the order of elements will
# be different . This is because sets dont have indexing and internally
# they use hashing for storing the elemens. As a result the index of 
# elements is not fixed.
s4 = {1,3,(1,3,1),"Hllo"} # this is allowed as sets allow immutable data type
print(s4)

# s5 = {1,32,{32,2}} # not possible as set itself is a mutable data type

s1 = {1,2,3,4,5}
# print(s1[0]) #sets dont allow indexing

# can we edit item in set?
# no we cant edit item in set. 
# s1[0] =5 #not allowed


# can we add item?
s1.add(6)

# print(s1)


# print(s2)
# del s2

# print(s1)
# s1.remove(6)
# print(s1)
# # pop is used to delete the last elements of the set. you might think theat
# # the elements which is at last of the set will be popped out but as we know that
# # internally sets used hashing as a result the first element will be delted not last
# s1.pop()
# print(s1) 

s1 = {1,2,3,4,5}
s2 = {3,4,5,6,7}

#these two are not allowed in set unlike the other containers like
# list , tuples ,stirngs etc.

# print(s1 + s2)
# print(s1 * 3)

for i in s1:
    print(i)
    
    
print(len(s1))
print(min(s1))
print(max(s1))
print(sum(s1))
print(sorted(s1))
print(sorted(s1,reverse = True))

print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s1.symmetric_difference(s2))
print(s1.isdisjoint(s2))
print(s1.issubset(s2))
print(s1.issuperset(s2))



