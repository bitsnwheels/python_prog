correctUsername = "campusx@gmail.com"
correctPassword = "1234"

username=input("Apna username bata:\n")
pw = input("ab chal password bata\n")

if(username==correctUsername and pw == correctPassword):
    print("Hlo & welcome")
elif username==correctUsername and pw!=correctPassword:
    print("Bhai tera password galat hai!")
    pw = input("Phir se password bata")
    if(pw==correctPassword):
        print("chal bhai tu andar aa hi gya")
    else:
        print("chala ja bsdk")
else:
    print("Chala ja BSDK")

