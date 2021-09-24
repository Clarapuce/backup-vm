def ContientE(mot):
    if "e" in mot : return True
    return False

def NbE(mot):
    nbE=0
    for i in mot: 
        if i=="e": nbE+=1
    return nbE

def ContientLettre(mot, lettre):
    for i in range(len(mot)) : 
        if mot[i]==lettre: 
            print("La lettre",lettre,"se trouve  la position",str(i+1))

def IndicesPaires(mot):
    carPaires=""
    for i in range (len(mot)):
        if i%2==0:carPaires+=mot[i]
    print(carPaires)


def ContientMaj(mot):
    for i in mot:
        if i.isupper():return(True)
    return(False)
print(ContientMaj("ab3j"))

def InsererAsterix(mot):
    motAsterix=""
    for i in mot:
        motAsterix +=i
        motAsterix+="*"
    return(motAsterix)

def InverserChaine(mot):
    motInverse = ""
    for i in reversed(range(len(mot))):
        motInverse += mot[i]
    return motInverse

def InverserChaine2(mot):
    motInverse = ""
    for i in range(len(mot)):
        motInverse += mot[len(mot)-i-1]
    return motInverse

def Palindrome(mot):
    motInverse = ""
    palindrome = False
    for i in reversed(range(len(mot))):
        motInverse += mot[i]
    if(mot==motInverse): palindrome = True
    return (motInverse,palindrome)