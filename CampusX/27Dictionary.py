#just like sets , dictionary has no indexing
# dicitionary is a mutable data type
# keys must be immutable but values can be both mutable and immutable
# keys should be unique

d= {} # this is an empty dictionary not a set
d1 = {"name": "John", "age": 30, "city": "New York"} 
# d2 = {[1,2,3]:"Ada"} # will throw an error as the key here is a list which is mutable

d2 = {(1,3,54):"Adarsh"} # this is valid

# wont throw an error but Rahul wiil be replaced by Rohit
d2 = ({"name":"Rahul","name":"Rohit"})
print(d2)

d3 = {"Name":"Rohit","College":"HIT","Marks":{"M1":56,"M2":66,"M3":78}}
print(d3)

# accessing elements from a dictionary
print(d3["Name"])
print(d3["College"])
print(d3["Marks"])
print(d3["Marks"]["M1"])


# how to edit
d3["Name"] = "Adarsh"
print(d3)

# add a new key value pair
d3['Age'] = 42
d3["Marks"]["M4"] = 70
print(d3)

# del d3
# del d3["College"]
# print(d3)

# d3.clear()
# print(d3)


# operations of dictionary

#these two are not allwed
# print(d1 + d2)
# print(d1 * 3)


# for i in d3:
#     print(i) # will print all the keys
# for i in d3:
#     print(d3[i]) # will print all the values
    
print("Adarsh" in d3) # will return false as "Adarsh" is not a key

print(len(d3))
print(min(d3))  # returns the lexicographically smallest key
print(max(d3))  # returns the lexicographically largest key
# print(sum(d3)) # only possible if the keys are only nubmers

print(sorted(d3))
print(sorted(d3,reverse=True))
print(d3.keys())
print(d3.values())