import random
ans = 56

count = 0  #number of steps taken as of now

low =1
high = 100
while(True):
    num = random.randint(low,high)
    print("The guessed number is ",num)
    if(num==ans):
        print("you guessed it right in ",count," number of steps")
        break
    else:
        if(num < ans):
            print("Guess Higher")
            low = num + 1
        else:
            print("Guess Lower")
            high = num-1
        count += 1
