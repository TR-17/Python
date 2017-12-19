def entree():
    a= int (input("a="))
    b= int (input("b="))
    return a,b

def calcul():
    c=10000
    d=10000;
    f=6.67*10**-11*(c*d/a**2)
    return f

def affichage():

    print("f","(",a,")",f)

a,b=entree();
while(a<b):
    f=calcul()
    affichage()
    a=a*2
