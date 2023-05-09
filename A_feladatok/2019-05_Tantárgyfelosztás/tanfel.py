#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# tanfel.py
# Érettségi feladat: 2019. május, Tantárgyfelosztás
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2019

#--- 1. feladat ---
adatok=[]
összes_óra=0
tanárok=set()  # készlet a 7. feladathoz
with open("beosztas.txt") as ff:
    k=1
    tétel=[]
    for line in ff:
        line=line.strip()
        if not line:
            continue
        if k%4:
            tétel.append(line)
            if k%4==1:
                tanárok.add(line)
        else:
            óraszám= int(line)
            összes_óra+= óraszám
            adatok.append(tétel+[óraszám])
            tétel=[]
        k+=1

#print(adatok)  #szemrevételezés

#--- 2. feladat ---
#print(f"2. feladat\nA fájlban {k//4} bejegyzés van.")
print(f"2. feladat\nA fájlban {len(adatok)} bejegyzés van.")

#--- 3. feladat ---
print(f"3. feladat\nAz iskolában a heti összóraszám: {összes_óra}")

#--- 4. feladat ---
print("4. feladat")
megadott_tanár= input("Egy tanár neve= ").strip().lower()
tanár_óraszáma=0
for tanár,tárgy,osztály,óraszám in adatok:
    if tanár.lower()==megadott_tanár:
        tanár_óraszáma+= óraszám

print(f"A tanár heti óraszáma: {tanár_óraszáma}")

#--- 5. feladat ---
with open("of.txt","w") as ff:
    for tanár,tárgy,osztály,óraszám in adatok:
        if tárgy=="osztalyfonoki":
            ff.write(f"{osztály} - {tanár}\n")

#--- 6. feladat ---
print("6. feladat")
megadott_osztály= input("Osztály= ").strip().lower()
megadott_tárgy= input("Tantárgy= ").strip().lower()
tsz=0
for tanár,tárgy,osztály,óraszám in adatok:
    if osztály.lower()==megadott_osztály and tárgy.lower()==megadott_tárgy:
        tsz+=1

print( "Csoportbontásban tanulják." if tsz>1 else "Osztályszinten tanulják.")

#--- 7. feladat ---
print(f"7. feladat\nAz iskolában {len(tanárok)} tanár tanít.")
#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben

