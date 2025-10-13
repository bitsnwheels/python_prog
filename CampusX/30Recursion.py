def multiply(a,b):
    result = 0
    for i in range(0,b):
        result = result + a
    print(result)

def multiplyRecursive(a,b,i):
    if(i==b):
        return 0
    return a + multiplyRecursive(a,b,i+1)
    
def checkPalindromeRecurive(text,i,j):
    if(i>j):
        return True
    else:
        if text[i] != text[j]:
            return False
        else:
            return checkPalindromeRecurive(text,i+1,j-1)

def fib(n):
    if n ==0 or n==1:
        return n 
    return fib(n-1)+fib(n-2)

def fbUsingMemoization(m,d):
    if m in d:
        return d[m]
    else:
        d[m] = fbUsingMemoization(m-1,d) + fbUsingMemoization(m-2,d)
        return d[m]



print(multiplyRecursive(8,9,0))
print(checkPalindromeRecurive("ababa",0,4))


d= {0:1,1:1}
print(fbUsingMemoization(500,d))

