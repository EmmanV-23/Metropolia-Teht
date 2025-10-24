def tulokset(lista):
    axed = [luku for luku in lista if luku % 2 != 0]
    return axed


#pääohjelma
luku=[]
while True:
    num = input("Anna luku (tyhjä lopettaa): ")
    if num  == "":
        break
    luku.append(int(num))

axed = tulokset(luku)
print("uusi lista", axed)