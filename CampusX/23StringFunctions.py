# c = "kolkata is in india"
# # print(len(c))
# # print(max(c))
# # print(min(c))
# # print(sorted(c)) #output will be in the form of a list
# print(c)


# capitalize / Title/Upper/Lower/Swapcase
# print(c.capitalize())
# print(c.title())
# print(c.upper())
# print(c.lower())
# print(c.swapcase()) # converts lower to upper and upper to lower


# #count funtion
# c="kolkata"
# print(c.count('a'))
# print(c.count('ata'))
# print(c.find('a'))
# print(c.find('ata')) # index where this part is present

# print(c.find('z')) # this will return -1
# # print(c.index('z')) # but in this case the code will break;

# print(c.endswith('a'))
# print(c.endswith('ata'))
# print(c.startswith('ko'))

# print("Hello my name is {} and I am {}".format("Nitish",30))
# print("Hello my name is {1} and I am {0}".format("Nitish",30))
# print("Hello my name is {name} and I am {age}".format(name="Nitish",age=30))
# print("Hello my name is {name} and I am {age}".format(name="Nitish",age=30,yoe = 2))


# c = "FLAT20"
# print(c.isalnum())
# print(c.isalpha())
# print(c.isdigit())
# print(c.isidentifier()) # whethe the stirng can be a valid varibale name or not
# print("21adf".isidentifier()) # whethe the stirng can be a valid varibale name or not



#split funtions

# c = "Who is the PM of India?"
# print(c.split()) 
# print(c.split('i'))
# print(c.split('Ind'))

# # join functions
# c= ['Who', 'is', 'the', 'PM', 'of', 'India?']
# print(" ".join(c))
# print("/ ".join(c))
# print("-".join(c))


# Replace Functions
c = "Hi My name is Adarsh"
print(c.replace("Adarsh","Adarsh Raj"))

#strip functions
c = "       HI my name is Adarsh        "
print(c)
print(c.strip())


