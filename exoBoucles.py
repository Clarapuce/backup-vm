
def AnneeBisextile(annee):
    if(annee%4==0):
        return(True if (annee%400==0) else False if (annee%100==0) else True )
    else : 
        return False

def JourDansMois(mois,annee):
    if(mois==2):
        return(29 if AnneeBisextile(annee) else 28)
    elif(mois<=7):
        return (30 if (mois%2==0) else 31)
    else :
        return (31 if (mois%2==0) else 30)
#trop complique, a refaire
def VerifierDate():
    date=""
    dateValide= False
    msg=""
    while not dateValide:
        date=input("Entrez une date (jj/mm/aaaa) : ")
        date.split("/")

        j=int(date[0])
        m=int(date[1])
        a=int(date[2])
        n=JourDansMois(m,a)
        dateValide = True
        if (date[0].isnumeric()):
            if not(1<=j<=n):
                print("Le jour doit etre compris entre 1 et "+ n)
                dateValide = False
        else : 
            print("Le jour doit etre un nombre")
            dateValide = False
        if (date[1].isnumeric()):
            if not(1<=j<=12):
                print("Le mois doit etre compris entre 1 et 12")
                dateValide = False
        else : print("Le mois doit etre compris entre 1 et 12")
        if (date[2].isnumeric()):
            if not(1900<=a<=2021):
                print("L'annee doit etre comprise entre 1900 et 2021")
                dateValide = False
        else : print("L'annee doit etre comprise entre 1900 et 2021")
    else : print("La date a bien ete prise en compte")

#Exercice 1
def LigneTirets():
    n=int(input("Entrez la longueur n de votre ligne de tirets : "))
    print("-"*n)

#Exercice 2
def CarreEtoile():
    n=int(input("Rentrez n : "))
    ligne="* " * n
    for i in range(n):
        print(ligne)

#Exercice 3
def CarreEntiersPositifs():
    for i in range (1,10):
        print(i,"au carre =",i*i)

#Exercice 4
def TableMultiplication():
    n=input("De quel nombre voulez-vous la table : ")
    while(not(n.isnumeric()) or not(0<int(n)<10)):
        n=input("Entree invalide. Veuillez entrer un chiffre entre 1 et 9 : ")
    for i in range(1,10):
        print(n,"*",i,"=",int(n)*i)

#Exercice 5
def MaxMinSommeMoy():
    nbMax=-10000
    nbMin=10000
    somme = 0
    n=input("Combien de nombres voulez-vous verifier ? : ")
    nb=0
    while(not(n.isnumeric()) or not(0<int(n))):
        n=input("Entree invalide. Veuillez entrer un nombre positif : ")
    for i in range(0,int(n)):
        nb=input("Nombre numero "+str(i+1)+" : ")
        while(not(nb.isnumeric())or not(0<int(n))):
            nb=input("Entree invalide. Veuillez entrer un nombre positif: ")
        somme += int(nb)
        if(int(nb)>nbMax):nbMax=int(nb)
        if(int(nb)<nbMin):nbMin=int(nb)
    print("Le maximum est : ",nbMax)
    print("Le minimum est : ",nbMin)
    print("La somme est : ",somme)
    print("La moyenne est : ",somme/int(n))

#Exercice 6
def Devinette():
    reponse = 3
    n=-1
    victoire=False
    print("Devinez le nombre de la machine (entre 0 et 20). Vous avez 5 essais.")
    for i in range(5):     
        n=input("Essai "+str(i+1)+": ")
        while(not(n.isnumeric()) or not(0<=int(n)<=20)):
            n=input("Entree invalide. Veuillez entrer un nombre entre 0 et 20 : ")
        
        n=int(n)
        if(n > reponse): print("Perdu ! Le nombre est plus petit ! ")
        elif(n < reponse) : print("Perdu ! Le nombre est plus grand !")
        else : 
            print("Bonne reponse ! Bravo ! ")
            victoire = True
            break
    if not(victoire):print("Vous n'avez plus d'essais. Vous avez perdu ! ")

#Exercice 7
def Somme():
    somme = 0
    n=input("Entrez n de la somme 1+2+3+...+n : ")
    while(not(n.isnumeric()) or not(0<int(n))):
        n=input("Entree invalide. Veuillez entrer un nombre positif : ")
    for i in range (1,int(n)+1):
        somme += i
    print("1+2+3+...+"+n+" = " +str(somme))
    print("1+2+3+...+"+n+" = n*(n+1)/2 = "+str(int(n)*(int(n)+1)/2)+" (formule mathematique)")

#Exercice 7 bis
def Harmonique():
    somme = 0
    n=input("Entrez n le rang du nombre harmonique Hn : ")
    while(not(n.isnumeric()) or not(0<int(n))):
        n=input("Entree invalide. Veuillez entrer un nombre positif : ")
    for i in range (1,int(n)+1):
        somme += 1/i
    print("Hn = " +str(somme))
    