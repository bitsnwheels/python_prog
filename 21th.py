# countries=("spain","italy","India","england","germany")
# temp=list(countries)  #will convert the tuple into list
# temp.append("Russia")  
# temp.pop(3)      #will remove the element at index 3 from the tuple
# temp[2]="finland"  
# countries=tuple(temp) #will convert the list "temp" into tuple
# print(countries)


        #methods in tuples

tup=(2,1,5,3,66,4,4,5,2)
print(tup.count(3))   #will print number of occurrences of element 3

pos=tup.index(5)   #will give the index where element 5 is present
print(pos)


