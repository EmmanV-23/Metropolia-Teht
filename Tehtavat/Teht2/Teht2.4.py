#Kirjoita ohjelma, joka kysyy kolme kokonaislukua.
# Ohjelma tulostaa lukujen summan, tulon ja keskiarvon.
import math

#Kysytään numero
print("Kirjoita kolme kokonaisluku: ")
one=(int(input("ensimmäisen numero: ")))
two=(int(input("ensimmäisen numero: ")))
three=(int(input("komlas numero: ")))

#kaavat
summa=(one+two+three)
tulo=(one*two*three)
keskiarvo=((one+two+three)//3)

#Vastaukset
print("summa:", summa)
print("tulo:", tulo)
print("keskiarvo:", keskiarvo)
