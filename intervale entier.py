def entree():
    a= int (input("a="))
    b= int (input("b="))
    c=0
    return a,b,c

def calcul(a,b,c):
    while(a<b):
        if(a%5==0):
            c=c+a
        a=a+1

    return c

def affichage(c):

    print("La somme est égale à :",c)

a,b,c=entree();
c=calcul(a,b,c);
affichage(c);
