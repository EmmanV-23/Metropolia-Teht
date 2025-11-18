#Sanakirja
lentoasemat = {}

while True:
    print("\nValitse toiminto:")
    print("1 = Syötä uusi lentoasema")
    print("2 = Hae lentoaseman tiedot")
    print("0 = Lopeta")

    valinta = input("Anna valinta: ")


    if valinta == "0":
        print("Ohjelma lopetettu.")
        break


    elif valinta == "1":
        icao = input("Anna lentoaseman ICAO-koodi: ")
        nimi = input("Anna lentoaseman nimi: ")
        lentoasemat[icao] = nimi
        print("Lentoasema tallennettu.")


    elif valinta == "2":
        icao = input("Anna haettava ICAO-koodi: ")
        if icao in lentoasemat:
            print("Lentoaseman nimi:", lentoasemat[icao])
        else:
            print("Koodia ei löytynyt.")


    else:
        print("Virheellinen valinta. Yritä uudelleen.")
