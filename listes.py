
def AfficherListe(liste):
    affichage=""
    for i in liste:
        affichage += " "+str(i)+" "
    return affichage

def AlternerMoisJour():
    t1=[31,28,31,30,31,30,31,31,30,31,30,31]
    t2=["Janvier","Fevrier","Mars","Avril","Mai","Juin","Juillet","Aout","Septembre","Octobre","Novembre","Decembre"]
    t3=[]
    for i in range (12):
        #t3 = t3 + [t2[i]]
        #t3 = t3+ [t1[i]]
        t3.append(t2[i])
        t3.append(t1[i])
    print(AfficherListe(t3))



def OneLineCarre():
    carre = [i ** 2 for i in range(1,6)]
    print(carre)
    carrePaire=[i**2 for i in range (1,6) if i%2==0]
    print(carrePaire)
    #Peut etre fait avec un pas

#Avec un oneline
def VerifPaire():
    valeurs = [i ** 2 for i in range(5)]
    print("valeurs contient " if len([x for x in valeurs if x%2==0])>0 else "valeurs ne contient pas", "des nombres pairs")

def PlusGrandElement(liste):
    max = liste[0]
    for i in liste:
        if(max<i):max = i
    return max

def TriPairesImpaires(liste):
    l1=[]
    l2=[]
    for i in liste:
        if i%2==0: l1.append(i)
        else: l2.append(i)
    return(l1,l2)

def TriMotsInf6(liste):
    l1=[]
    l2=[]
    for i in liste:
        if len(i)>=6: l1.append(i)
        else: l2.append(i)
    return(l1,l2)

