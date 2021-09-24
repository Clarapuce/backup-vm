def NombrePremier(x):
    for i in range(2,x):
        if(x!=i) and(x%i==0):return False
    return True

def GenererNbPremiers(x):
    for i in range(1,x):
        if NombrePremier(i): yield i


def Fibonacci(n):
    if(n==0):return 0
    if(n==1):return 1
    u=Fibonacci(n-1)+Fibonacci(n-2)
    return u

def GenererFibonacci(n):
    for i in range(n+1):
        yield Fibonacci(i)
    #yield ( Fibonacci(i) for i in range(n+1) )

for k in GenererFibonacci(5):
    print(k)