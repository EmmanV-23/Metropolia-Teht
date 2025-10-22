luku =  []

while True:
    num = input("Anna luku (tyhjä lopettaa): ")
    if num  == "":
        break

    luku.append(int(num))

luku.sort(reverse=True)

print("Viisi suurinta lukua ovat:")
for vastaus in luku[:5]:
    print(vastaus)



