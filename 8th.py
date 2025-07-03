# author:Adarsh Raj
# 31st march,2023

# in this lecture we are going to study about string slicing
str = "adarsh_raj"
print(len(str))
print(str[0:10])  # including index 0 but excluding 10
print(str[:10])  # will print the same result as previous case
print(str[:])  # will print the same result as previous case
print(str[0:4])  # will print the charcaters from index 0 to index 3

print(str[-5:10])  # here -5 means (len(str)-5)
print(str[5:-2])  # here also -2 means (len(Str)-2)
