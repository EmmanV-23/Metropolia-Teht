import random

#Kirjoita ohjelma, joka arpoo ja tulostaa kaksi erilaista numerolukon koodia:
#kolmenumeroisen koodin, jonka kukin numeromerkki on väliltä 0..9.
#nelinumeroisen koodin, jonka kukin numeromerkki on väliltä 1..6.

#kolmenumeroinen
nro=str(random.randint(0,9))
nro=nro+str(random.randint(0,9))
nro=nro+str(random.randint(0,9))
print("kolmenumeroinen: ", nro)

#nelinumeroinen
num=str(random.randint(1,6))
num=num+str(random.randint(1,6))
num=num+str(random.randint(1,6))
num=num+str(random.randint(1,6))
print("nelinumeroinen:", num)



