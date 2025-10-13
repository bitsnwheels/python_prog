# c="hellow"
# print(c)
# print(c[5])  # positive indexing
# print(c[-1]) #negative indexing


#string slicing
c = "Hellow World"
# print(c[2:])
# print(c[:4])
# print(c[:])
# print(c[2:7:2]) #last one is the step 
# print(c[::-1])

print(c[-1:-13:-1])

c = [12,24,1,15,67]
for i in range(len(c)//2):
    c[i],c[len(c)-1-i]=c[len(c)-1-i],c[i]

print(c)

print(5/2)
print(5//2)
print(5 %2)
print(round(5/2))

