# a = 5
# b = a

# del a
# print(b)  #still prints 5 as b still points to the memory location of 5 

# a = 5
# b = a
# a = 6
# print(b)  # still prints the old value of a which was five


# import sys
# a = "adfjkjd l lkdf ad "
# b = a
# c = b
# print(id(a),id(b),id(c))  #all of them point to the same memory location
# print(sys.getrefcount(a))  # number of references at a memory location


L = [11,2,3]
print(id(L))

#both of them will be same
print(id(L[0]))
print(id(11))

#both of them will be same
print(id(L[1]))
print(id(2))  



# l1 = [1,2,3]
# l2 = l1
# l1.append(4)
# print(l1)
# print(l2)
#in the above case 4 will be appended to both l1 and l2


#in the below case the changes done in l2 wont reflect
# in l1 as we did cloning
# l1 = [1,2,3]
# l2 = l1[:] #cloning              
# l2.append(4) 
# print(l1)
# print(l2)

# l1 = [1,3,231,5,(13,53)]
# l1[-1][-1] = 599  # this will throw an error as even though we are working with list still the changes which we are trying to do is in tuple which is not allowed.
# print(l1)  

v1 = (1,3,32,5,[5,51,13])
v1[-1][-1] = 341 # this is completely legal because even though we are working with tuples still the final changes being done are in a list not in tuple.
print(v1) 






