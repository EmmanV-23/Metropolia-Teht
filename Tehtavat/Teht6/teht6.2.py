#Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän.
#Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa.
#Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku,
#joka kysytään käyttäjältä ohjelman suorituksen alussa.
import random

def noppa(tahkot):
    silmaluku = random.randint(1, tahkot)
    return silmaluku

#Pääohjelma
tahkot = int(input("Tahkojen määrä? : "))
silmaluku = 0

while silmaluku != tahkot:
    silmaluku = noppa(tahkot)
    print("Heitit: ", silmaluku)
    if silmaluku == tahkot:
            print("Critical hit!!!")
