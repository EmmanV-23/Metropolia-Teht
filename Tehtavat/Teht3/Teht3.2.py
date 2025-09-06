#Kirjoita ohjelma, joka kysyy käyttäjältä laivan hyttiluokan
# (LUX, A, B, C) ja tulostaa sen sanallisen kuvauksen alla olevan luettelon mukaisesti.
# Tehtävässä on käytettävä if/elif/else-toistorakennetta.

# LUX on parvekkeellinen hytti yläkannella.
#A on ikkunallinen hytti autokannen yläpuolella.
#B on ikkunaton hytti autokannen yläpuolella.
#C on ikkunaton hytti autokannen alapuolella.

print("Valitse hyttiluoka:\n A: A \n B: B "
      "\n C: C \n D: Lux")

valinta = input("Valintasi (A - D): ")

if valinta == "A":
    print("A ikkunallinen hytti autokannen yläpuolella.")
elif valinta == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif valinta == "C":
    print("C on ikkunaton hytti autokannen alapuolella")
elif valinta == "D":
    print("LUX on parvekkeellinen hytti yläkannella.")
else:
    print("Virheellinen hyttiluokka")