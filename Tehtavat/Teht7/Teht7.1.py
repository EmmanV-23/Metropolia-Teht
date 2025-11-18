vuodenajat = ("talvi", "kevät", "kesä", "syksy")

kuukausi = int(input("Anna kuukauden numero (1–12): "))


if kuukausi == 12 or kuukausi == 1 or kuukausi == 2:
    vuodenaika = vuodenajat[0]   # talvi
elif kuukausi == 3 or kuukausi == 4 or kuukausi == 5:
    vuodenaika = vuodenajat[1]   # kevät
elif kuukausi == 6 or kuukausi == 7 or kuukausi == 8:
    vuodenaika = vuodenajat[2]   # kesä
elif kuukausi == 9 or kuukausi == 10 or kuukausi == 11:
    vuodenaika = vuodenajat[3]   # syksy
else:
    vuodenaika = "virheellinen kuukausi"

print("Vuodenaika on:", vuodenaika)
