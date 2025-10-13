l1 = [1,2,3,[3,4]]
print(l1[3][1])
print(l1[-1][-1])

# 3d list

l2 = [ [ [1,2],[3,4] ],[ [5,6],[7,8]],[[9,10],[11,12] ] ]
print(l2[-1][-1][0])

# list in python are mutable
l=[1,2,3,4,5]
print(l)
l[0] = -1
print(l)

# adding into the string
    #append
l.append(1000)  # appends expects one item
l.extend([2000,3000,4000]) # extend expects a list of item
l.append([20,30]) #type:ignore  # for ignoring the error from pylane

l.insert(1,'world') #type:ignore


# Deleting from a list

# del
del l1 
del l[0]
del l[-1] 
print(l)

del l[-1:-4:-1]

l.remove('world')  #type:ignore
l.pop()
# l.clear()
print(l)


l1 = [12,2,4,1]
l2 = [24,1,1,1]
print(l1+l2)
print(l1 * 3)
print(len(l1))
print(min(l1))
print(max(l1))
print(l1)
print(sorted(l1,reverse = True)) # not permanent ie. original lsit is as it si
print(l1)
l1.sort(reverse=True) # here the changes are permanent
print(l1)

print(l1.index(4))






