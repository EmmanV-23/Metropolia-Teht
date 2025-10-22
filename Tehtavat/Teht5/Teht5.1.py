import random

arpakuutio = int(input("Kuinka monta arpakuutioita heitetään? "))

total = 0

for i in range(arpakuutio):
    silmaluku = random.randint(1,6)
    total += silmaluku

print("Silmälukujen summa on: ", total)


