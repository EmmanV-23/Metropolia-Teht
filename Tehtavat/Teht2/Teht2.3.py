#Kirjoita ohjelma, joka kysyy suorakulmion kannan ja korkeuden.
# Ohjelma tulostaa suorakulmion piirin ja pinta-alan.
# Suorakulmion piiri tarkoittaa sen neljän sivun yhteispituutta

import math
#Pinta-alan laskukaava : kanta*korkeus
#Piiri laskukaava: 2*kanta+2*korkeus

kanta=int(input("Suorakulmion kanta:"))
korkeus=int(input("Suorakulmion korkeus:"))

pintaala=(kanta*korkeus)
piiri=(2*kanta+2*korkeus)

print("suorakulmion pintaala: ",pintaala)
print("suorakulmion piiri: ",piiri)




