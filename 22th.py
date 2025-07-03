print("Welcome to KBC")


list1 = ["PM of India", "CM of Bihar", "CM of UP", "CM of DELHI"]
list2 = ["NARENDRA MODI", "NITISH KUMAR", "YOGI ADITYANATH", "ARVIND KEJRIWAL"]

amount = 0

length = len(list1)
for i in range(length):
    print("Who is ", list1[i], "?")
    ans = input()
    ans1 = ans.upper()
    if (ans1 == list2[i]):
        amount = amount+10
    else:
        break

print("You have won ", amount, "points")
