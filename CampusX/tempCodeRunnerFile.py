
L=[1,2,3,4,5,6,7]
# In map, when we pass a lambda function and an iterable then we can apply that lambda function on each element of that iterable
print(map(lambda x:x*2,L))
print(list(map(lambda x:x*2,L)))
print(list(map(lambda x:x%2==0,L)))