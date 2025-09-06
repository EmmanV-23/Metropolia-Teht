

#Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l).
# Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.

#Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
#Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.

print("Valitse sukupuoli:\n A: Nainen \n B: Mies ")
valinta=input("Valintasi (A-B):")

arvo=int(input("Kerro hemoglobiiniarvo: "))


if valinta == "A": #Naienn arvo
    if arvo < 117:
        print("Hemoglobiini taso on alhainen")
    elif arvo > 175:
        print("Hemoglobiini taso on korkea")
    else:
        print("Hemoglobiini taso on normaali")
if valinta == "B":  #Mies arvo
    print(int(input("kerro hemoglobiiniarvo")))
    if arvo < 134:
        print("Hemoglobiini taso on alhainen")
    elif arvo > 195:
        print("Hemoglobiini taso on korkea")
    else:
        print("Hemoglobiini taso on normaali")


