
#Exercice 1
def RegleGraduee():
    n=int(input("Entrez la longueur n de votre ligne de tirets : "))
    print("-"*n)

#Exercice 2
def CarreEtoile():
    
    n=int(input("Rentrez n : "))
    for i in range(n):
        for j in range(n):
        print("*"*)

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
        if(int(n) > reponse): print("Perdu ! Le nombre est plus petit ! ")
        elif(int(n) < reponse) : print("Perdu ! Le nombre est plus grand !")
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
    
Harmonique()