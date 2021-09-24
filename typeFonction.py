def Factorielle(n):
    if(n==1):return 1
    else : return n* Factorielle(n-1)

def TypeVar(*args):
    typeVar = [type(i).__name__ for i in args]
    nbType=[]
    nbType = [typeVar.count(k) for k in typeVar if k not in nbType]
    listeType=[]
    for i in range(len(typeVar)):
        if typeVar[i] not in listeType:
            listeType.append(typeVar[i])
            listeType.append(nbType[i])

    return (listeType)


def Somme(a,b):
    return a+b
def Produit(a,b):
    return a*b
def Operation(a,b,c,op1,op2):
    return(op2(op1(a,b),c))

print(Operation(2,3,2,Somme,Produit))
