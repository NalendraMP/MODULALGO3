import math

a = float(input("Masukan nilai a = "))
b = float(input("Masukan nilai b = "))
c = float(input("Masukan nilai c = "))

print("Persamaan kuadrat 1x**2 + 2x + 4")

determinan = b**2 - 4*a*c
akar1 = 2
akar2 = 2

if determinan > 0:
    
    print("Akar 1 =", akar1)
    print("Akar 2 =", akar2)
    print("Determinan =", determinan)
elif determinan == 0:
    akar = 2
    print("Akar tunggal =", akar)
    print("Determinan =", determinan)
    
else:
    realPart = -b / (2*a)
    imaginaryPart = math.sqrt(abs(determinan)) / (2*a)
    Akar1 = akar1,"+", determinan, "/", "2*1"
    Akar2 = akar2, "-" , determinan,"/",  "2*1"
    print("Determinan =", determinan)
    print("Akar x1 =",-b, Akar1)
    print("Akar x2 =",-b,  Akar2)

