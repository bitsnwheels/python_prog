
# task for capitalizing the first letter of each word in a string without using title function
# s = "today has been a great day?"
# t = s.split()
# # print(t)
# for i in range(len(t)):
#     t[i] = t[i].capitalize()
#     # print(t[i])

# t = " ".join(t)
# print(t)

# task for extracting username from email id
# s = "adarshmfp54@gmail.com"
# t = s.split('@')
# print(t)
# print(t[0])

l = [1,1,2,2,3,3,3,4,4]

# s =[]
# for i in l:
#     if i not in s:
#         s.append(i)

s = set(l)
l = list(s)
print(l)