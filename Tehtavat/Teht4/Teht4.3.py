#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.
from enum import nonmember

pienin = None
suurin = None

while True:
    num = input("Anna luku (tyhjä lopettaa):")
    if num == "":
        break

    luku = int(num)

    if pienin is None or suurin is None:
        pienin = luku
        suurin = luku

    else:
        if luku < pienin:
            pienin = luku
        if luku > suurin:
            suurin = luku

if pienin is not None:
    print("Peinin luku:", pienin)
    print("Suurin luku:", suurin)

else:
    print ("Lukuja ei annettu")

