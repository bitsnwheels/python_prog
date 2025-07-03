#here we are going to study about docstrings in python
#python docstrings are the string literals that appear right after the definition of a function,method,class,or module
#docstrings are different from comments because comments are completely igonored while these are not!
#we can also print docstrings but not comments

def square(n):
    '''takes an input and returns its square
    '''
    print(n**2)
square(5)
print(square.__doc__)   #it will print takes an input and returns its square

# note: if we change the position of the docstring then that is not considered as a docstring


          #PEP8
        # pep8 is a document that provides guidelines and best practices on how to 
        # write python code.The primary focus  of pep8 is to improve the readibility
        # and consistency of python code
        
        