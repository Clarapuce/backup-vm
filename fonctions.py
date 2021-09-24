
def Factorielle(n):
    fact = 1
    for i in range (1,n+1):
        fact*=i
    return fact


def Somme(n):
    somme = 0
    for i in range (1,n+1):
        somme+=i
    return somme


def Puissance(a,n):
    puis = 1
    for i in range (1,n+1):
        puis*=a
    return puis

def Exponentielle(x):
    exp = 0
    for n in range (50):
        exp+=Puissance(x,n)/Factorielle(n)
    print("exp("+str(x)+") = "+str(exp))

def Sinus(x):
    sin = 0
    for n in range (50):
        sin += Puissance(-1,n)*(Puissance(x,2*n+1)/Factorielle(2*n+1))
    print("sin("+str(x)+") = "+str(sin))

def Pi():
    pi=0
    for k in range (50):
        pi += (Puissance(2,k)*Puissance(Factorielle(k),2))/(Factorielle(2*k+1))
    pi=pi*2
    print(pi)
Pi()