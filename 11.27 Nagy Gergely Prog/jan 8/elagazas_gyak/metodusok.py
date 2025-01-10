def feladat1():
    szam = int(input("Egész szám: "))
    if szam % 2 == 0:
        print("Páros:" , szam)
    else:
        print("Páratlan:" , szam)

def feladat2():
    szam= float(input("Valós szám: "))
    if szam >=0:
        print(szam)
    else:
        print(szam*-1)

def feladat3():
    szam= float(input("Valós szám: "))
    if szam <=0:
        print("hiba a kör sugara nem pozitív")
    else
        print("Kör területe", szam*szam*3.14)

def feladat4():
    korsugara = float(input("Add meg a kör sugarának értékét"))