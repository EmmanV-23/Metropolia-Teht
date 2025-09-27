# Kirjoita ohjelma,
# joka muuntaa tuumia senttimetreiksi niin kauan kunnes käyttäjä antaa negatiivisen tuumamäärän.
# Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm

while True:
    tuumat = float(input("Anna tuumat: "))
    if tuumat < 0:
        print("Ohjelma lopetetaan.")
        break

    sentit = tuumat * 2.54
    print(f"{tuumat} tuumaa = {sentit:.2f} cm")
