#Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10.
# Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein.
# Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus, Liian pieni arvaus tai Oikein.
#Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.
import random


numerot = random.randint(1, 10)

print("Arvaa luku (1-10):")

while True:
    arvaus = int(input("Anna arvauksesi: "))

    if arvaus == numerot:
        print("Oikein!")
        break
    elif arvaus > numerot:
        print("Liian suuri arvaus")
    else:
        print("Liian pieni arvaus")
