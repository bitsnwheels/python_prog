t1 = ()
t2 =(1,3,3,6,5)
t3 = (1,3,4,5)
t4 = (1,2,3,(4,5))
t5 = (1,3,2,"hlo",True)

# t5 =(1) # this is not a tuple. The synatx for single item tuple is bit differnet from normal tuple

t5 =(1,) # this is a valid syntax for single item tuple.
print(type(t5))

print(t4[0])

# the tuple is immutable just like strings.
# t4[0]= 100 #not allowed in tuple
# editing is not allowed in tuples but deletion of the whole tuple is allowed

# del t4
# print(t4) # will throw an error

# del t4[-1] # this is also not allowed.

# print(t2 +t3)
# print(t3 * 3)

# for i in t2:
#     print(i)

print(len(t3))
print(min(t3))
print(max(t3))
print(sum(t3))
print(sorted(t2))
print(sorted(t2,reverse=True))
print(t2)
