# author:adarsh raj
# date:12th apr,2023

# try:
#     l = [3, 5, 6]
#     x=int(input("Enter the value of index:"))
#     print(l[x])
# except:
#     print("some error occured")
    
# finally:     #code inside finally block is implemented irrespective of the error occured
#     print("I am always executable")
"""
the above finally block can be implemented even if we simply write a print statement as done 
below so you might be wondering what will be the use of finally block.Well the finally block is used when
we have to return a value in a function.just loook at the example below
"""
# print("I am always executable")



def func1():
    try:
        l=[3,5,6]
        x=int(input("Enter the value of index:"))
        print(l[x])
        return 1
    except:
        print("some error occured")
        return 0
    finally:
        print("I am always executable")
    
    print("i am always execuable")   #here this statement wont be printed when this fucntion will be called but if we use the finally block then this statement will be printed
    
    
    
x=func1()
print(x)
        

    


    
    

 