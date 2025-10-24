#parametrit

def bensa(gallon):
    litra = gallon * 3.785
    return litra

#Pääohjelma



while True:
    gallon = float(input("Anna bensiini määrä, negatiivinen lopettaa ohjelma: "))
    if gallon < 0:
        print("Error")
        break
    litra = bensa(gallon)
    print("Bensiini määrä litroina: ", litra)


