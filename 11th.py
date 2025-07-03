import time
timestamp=time.strftime('%H:%M:%S')
print(timestamp)
timestamp=int(time.strftime('%H'))

if(timestamp>=6 and timestamp<=12):
    print("Good Morning")
else:
    print("Its not morning")
