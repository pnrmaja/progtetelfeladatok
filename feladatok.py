import math

def feladat1():
    db:int= 0
    i: int =1
    while (i <= 1000):
        if (i%7==0):
            db=db+1


        i=i+1
    print(f" Ennyi osztható  szám van 7-el: {db}")

def feladat2():
    db:int= 0
    i:int= 2000
    while (i<=20000):
        if (i%12==0):
            db=db+1


        i=i+1

    print(f"12-vel osztható szám: {db}")

def feladat3():
    db=0
    szam=1
    osszeg=0
    while (db<20):
        if (szam%3==0):
            osszeg=osszeg+math.pow(szam,2)
            db=db+1

        szam=szam+1
    print(f"Az első 20 3-mal osztható szám négyzetének összege: {osszeg}")

def feladat4(szam):
    i:int= 1
    while (i<szam):
        if (szam%i==0):
            print(f" A {szam} egész osztója {i}")
        i=i+1

def feladat5(szam):
    max:int=-1
    i:int= 1
    while (i<szam):
        if ( szam%i==0):
            if (i>max):
                max=i
        i=i+1

    print(f" A {szam} legnagyobb egész osztója: {max}")


