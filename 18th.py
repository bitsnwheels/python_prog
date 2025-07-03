marks=[3,5,6,"harry",True]
print(marks)

# for i in range(len(marks)):
#     print(marks[i])
    
# print(marks[-3])   #negative indexing is used in this case also

                #we can also search in indexing with the help of below code
# if 5  in marks:
#     print("yes")

# if "harry" in marks:
#     print("yes")



                 #we can also use the same pattern for strings also as shown belwow
# str="adarsh"
# if "ad" in str:
#     print("yes")



                #we can also use slicing as we used to do in strings

# print(marks[:])
# print(marks[1:5])  #will print from index 1 to 4
# print(marks[:5:2])  #here "2" is used to skip the content as we used to do in loops




                 #now we are going to use list comprehension.list comprehension is used for creating new lists from other iterables like lists,tuples,dictionaries,sets,and even in arrays and strings

lst=[i for i in range(3)]
print(lst)    #will print 0,1 and 2

lst=[i for i in range(10) if i%2==0]
print(lst)    #will print all the even numbers from 0 to 8 including 0
