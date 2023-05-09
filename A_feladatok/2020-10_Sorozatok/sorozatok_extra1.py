#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# sorozatok_extra1.py
# Érettségi feladat: 2020. október, Sorozatok
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2020

import datetime as dt

#--- 1. feladat ---
sorozatok=[]
with open("lista.txt") as ff:

    l=[] # [ datetime(2017,07,16)/NI, Games, 7x01, 60, 1/0 ]
    dátumos=0
    megnézett=0
    időtöltés=0 # percek
    for sorszám,sor in enumerate(ff):

        sor= sor.strip()
        l.append(sor)

        if sorszám%5 == 4:

            sorozatok.append(l)
            if l[0]!="NI":
                dátumos+= 1
                l[0]= dt.datetime.strptime(l[0],"%Y.%m.%d")

            if l[-1]=="1":
                megnézett+= 1
                időtöltés+= int(l[-2])

            l=[]

#print(sorozatok)

#--- 2. feladat ---
print(f"2.feladat\nA listában {dátumos} db vetítési dátummal rendelkező epizód van.\n")

#--- 3. feladat ---
print(f"3. feladat\nA listában lévő epizódok {megnézett/len(sorozatok):.2%}%-át látta.\n")

#--- 4. feladat ---
tidő= dt.timedelta(minutes=időtöltés)
print(f"4. feladat\nSorozatnézéssel {tidő.days} napot {tidő.seconds//3600} órát és {tidő.seconds%3600//60} percet töltött.\n")

#--- 5. feladat ---
megadott_dátum= input("5. feladat\nAdjon meg egy dátumot (éééé.hh.nn)! Dátum= ").strip()
megadott_dátum= dt.datetime.strptime(megadott_dátum,"%Y.%m.%d")

for dátum,cím,epizód,perc,megtekintett in sorozatok:

    if dátum=="NI":
        continue
    if megadott_dátum >= dátum and megtekintett=="0":
        print(f"{epizód}\t{cím}")

print()

#--- 6. feladat ---
# Nem szükséges.

#--- 7. feladat ---
megadott_nap= input("7. feladat\nAdja meg a hét egy napját (például cs)! Nap= ").strip()
adott_napon= set()
hét_napja=["h","k","sze","cs","p","szo","v"]

for dátum,cím,epizód,perc,megtekintett in sorozatok:

    if dátum=="NI":
        continue
    if megadott_nap == hét_napja[dátum.isoweekday()-1]:
        adott_napon.add(cím)

if not adott_napon:
    print("Az adott napon nem kerül adásba sorozat.")
else:
    print(*adott_napon, sep="\n")

#--- 8. feladat ---
summa= dict()   # cím --> [percek,epizódok_száma]
for dátum,cím,epizód,perc,megtekintett in sorozatok:

    perc= int(perc)
    if cím not in summa:
        summa[cím]= [perc,1]
    else:
        summa[cím][0]+= perc
        summa[cím][1]+= 1

with open("summa.txt","w") as ff:

    for cím,(perc,db) in summa.items():
        ff.write(f"{cím} {perc} {db}\n")

#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben
