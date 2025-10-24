#Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan silmäluvun väliltä 1..6.
#Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen.
#Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.

import random
import math

#funktio
def noppa():
    return random.randint(1,6)

#Pääohjelma

silmaluku = 0
while silmaluku != 6:
    silmaluku = noppa()
    print("Heitit: ", silmaluku)
    if silmaluku == 6:
            print("Lucky number.")
