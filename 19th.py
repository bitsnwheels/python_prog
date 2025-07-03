# author:adarsh raj
# date:2nd apr,2023

# same as strings,list also has a lot of methods and we dont need to remember all of these as interntet is always there.although some of them have been discussed below


l = [2, 43, 11, 7, 35, 5]
print(l)
# l.append(7) #will add the parameter at the end
# print(l)

# l.sort()    #will sort the elements in ascending order
# print(l)

# l.sort(reverse=True)       #will sort the elements in descending order
# print(l)

# l.reverse()   #will reverse the given string
# print(l)

# print(l.index(7))   #will print the index of the given value in the list
# print(l.count(7))    #will print the number of occurences of 7 in the list

# doing so will change the oringinal list
# m=l
# m[0]=5
# print(l)   #will print the modified value of l 

# the above problem is solved with the help of below code

# m = l.copy()
# m[0] = 5
# print(l)   #will print the original value of l


# l.insert(1,899)   #will insert 899 at index 1

# m=[900,1000,1100]
# l.extend(m)        # will append the values of list m to list l


print(l)

