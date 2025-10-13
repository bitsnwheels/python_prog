#arithmetic operators
s = "hello"
t = "hi"
print(s+" "+t)
print(s*5)

#lexicographical comparsion
print(s>t)
print(s==t)
print(s!=t)
print(s<t)

#logical operations on strings
print(t and s)
print("" and "adf")
print("" or "adf")
print("adf" or " ")
print(not "hello") # not 1
print(not "") # not 0

for i in s:
    print(i)

print('c' in s)
print('h' in s)
print('hellow' in s)
print('hello' in s)
