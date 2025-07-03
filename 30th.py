# author:adarsh raj
# date:11apr,2023
  #we know that we can use else with while loop but we can also use it with for loop 
"""
for i in range(10):
    print(i)
    
else:
    print("loop is over") #in this case once the loop is over then control will move to else and "loop is over" will be printed
    
"""

 

for i in range(10):
    print(i)
    if(i==5):
        break
    
else:
    print("loop is over")    #in this case once the loop is terminated then control will not move to else block as we have used break statement and will simply not print what is written in else block