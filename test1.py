#cas classique
def classique():
    x=-10
    if(x>0):
        print(str(x),'est positif.')
    elif (x==0):
        print(str(x),"est nul.")
    else :
        print(str(x),"est negatif.")

#avec les one line if
def oneline():
    x=0
    print(str(x)+' est positif' if (x>0) else str(x)+' est negatif' if (x<0) else str(x)+ " est nul")
