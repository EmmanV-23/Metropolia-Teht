#Kirjoita ohjelma, joka kysyy käyttäjältä massan keskiaikaisten mittojen
# mukaan leivisköinä, nauloina ja luoteina.
# Ohjelma muuntaa syötteen täysiksi kilogrammoiksi ja grammoiksi sekä ilmoittaa tuloksen käyttäjälle.
#Yksi leiviskä on 20 naulaa.
#Yksi naula on 32 luotia.
#Yksi luoti on 13,3 grammaa.

import math
one = float(input("Luoti: "))
dos = float(input("Naulaa: "))
three = float(input("Leiviskaa: "))
#Kaavojen ehdot

luoti=(13.3*one)
naula=((13.3*32)*dos)
leiviska=((13.3*32)*20)*three

kokonaispaino=luoti+naula+leiviska

kg = int(kokonaispaino//1000)
g = kokonaispaino%1000

print(f"Luodin paino:, {luoti:.2f}," "grammaa")
print(f"Naulan paino:, {naula:.2f}" "grammaa")
print(f"Leiviskän paino:, {leiviska:.2f}","grammaa")
print("Yhteensä:", kg, "kilogramma")

#round komento on haettu netistä
print("Eli:",kg,"kilogramma ja",round(g,2),"grammaa")



