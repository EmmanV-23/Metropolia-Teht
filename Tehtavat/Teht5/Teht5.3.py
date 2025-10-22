luku = int(input("Anna luku:"))

if luku > 1:
    for i in range(2, luku):
        if luku % i == 0:
            print("Ei ole alkuluku")
            break

    else:
        print("Numero on alkuluku")
