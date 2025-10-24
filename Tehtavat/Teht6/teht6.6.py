import math


def paras(halkaisijacm, hintae):
    sade = (halkaisijacm/2)/100 # halkaisija metreiksi, jotta saadaan sade
    area = math.pi * (sade**2)  #pinta ala neliömeteinä
    total = hintae * area
    return total

#Pääohjelma
print("Anna ensimmäinen pizzan tiedot:")
sade1 = int(input("Halkaisija (cm):"))
hinta1 = int(input("Hinta (euroina):"))

print("\nAnna toisen pizzan tiedot:")
sade2 = int(input("Halkaisija (cm):"))
hinta2 = int(input("Hinta (euroina):"))

first = paras(sade1, hinta1)
second = paras(sade2, hinta2)

print("\nPizza 1: hinta per neliömetri on:",first )
print("Pizza 2: hinta per neliömetri on:", second )

if first < second:
    print("Pizza 1 antaa paremman vastineen rahalle.")
elif second < first:
    print("Pizza 2 antaa paremman vastineen rahalle.")
else:
    print("Sama hintalaatusuhde")
