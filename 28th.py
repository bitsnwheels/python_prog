# author:adarsh raj
# date:11th apr,2023


"""
dictionaries are ordered collection of data items.They store multiple items in a single varible.dictionary items are key-value
pairs that are separated by commas and enclosed within curly brackets.
"""
info={"name":"Adarsh Raj","Age":45,"eligible":True}
print(info)

#we can get the value of a key using the below methods:

"""
print(info["name"])
     # or 
print(info.get("name"))

"""

"""
          #we can get all the keys with the below method:
print(info.keys())
          #we can also get all the values with the below method:
print(info.values())

"""

for key in info.keys():
    print(f"The value for key  {key} is {info[key]}") 