#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# sorozatok.py
# Érettségi feladat: 2020. október, Sorozatok
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2020

#--- 1. feladat ---
sorozatok=[]
with open("lista.txt") as ff:

    l=[] # [ 2017.07.16/NI, Games, 7x01, 60, 1/0 ]
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

            if l[-1]=="1":
                megnézett+= 1
                időtöltés+= int(l[-2])

            l=[]

#print(sorozatok)

#--- 2. feladat ---
print(f"2.feladat\nA listában {dátumos} db vetítési dátummal rendelkező epizód van.\n")

#--- 3. feladat ---
print(f"3. feladat\nA listában lévő epizódok {round(megnézett/len(sorozatok)*100,2)}%-át látta.\n")

#--- 4. feladat ---
napok= időtöltés//(24*60)
órák= időtöltés%(24*60)//60
percek= időtöltés%60
print(f"4. feladat\nSorozatnézéssel {napok} napot {órák} órát és {percek} percet töltött.\n")

#--- 5. feladat ---
megadott_dátum= input("5. feladat\nAdjon meg egy dátumot (éééé.hh.nn)! Dátum= ").strip()
for dátum,cím,epizód,perc,megtekintett in sorozatok:
    """
    A dátum olyan karakterláncként van ábrázolva, hogy az összehasonlításuk helyes
    eredményt ad dátum-objektummá konvertálás nélkül is:
        "09.10" < "12.10" (de: "9.10" > "12.10" lenne)
    """
    if dátum == "NI":
        continue
    # Az előző vizsgálat el is hagyható, mert ha a dátum=="NI", akkor
    # a megadott_dátum >= dátum állítás mindig hamis lesz, pl. a "2017.10.01" < "NI"
    # fog fenn állni, mert az "N" karakterlánc kódértéke mindig nagyobb egy szám
    # kódértékénél. Tehát az "NI"-s filmek nem kerülnek kiírásra, ami megfelel a
    # feladat megfogalmazásának.
    if megadott_dátum >= dátum and megtekintett=="0":
        print(f"{epizód}\t{cím}")

print()

#--- 6. feladat ---
"""
Függvény hetnapja(ev, ho, nap : Egész) : Szöveg
    napok: Tömb(0..6: Szöveg)= ('v', 'h', 'k', 'sze',
                                'cs', 'p', 'szo')
    honapok: Tömb(0..11: Egész)= (0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4)
    Ha ho < 3 akkor ev := ev -1
    hetnapja := napok[(ev + ev div 4 – ev div 100 +
                       ev div 400 + honapok[ho-1] + nap) mod 7]
Függvény vége
"""
def hétnapja(év, hó, nap):

    napok= ["v","h","k","sze","cs","p","szo"]
    hónapok= (0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4)
    if hó < 3:
        év= év-1
    hétnapja= napok[ (év+év//4-év//100+év//400+ hónapok[hó-1]+nap)%7 ]

    return hétnapja

#--- 7. feladat ---
megadott_nap= input("7. feladat\nAdja meg a hét egy napját (például cs)! Nap= ").strip()
adott_napon= set()
for dátum,cím,epizód,perc,megtekintett in sorozatok:

    if dátum=="NI":
        continue
    év,hó,nap= dátum.split(".")
    if megadott_nap == hétnapja(int(év),int(hó),int(nap)):
        adott_napon.add(cím)

if not adott_napon:
    print("Az adott napon nem kerül adásba sorozat.")
else:
    for cím in adott_napon:
        print(cím)

# Megjegyzés a 7. feladathoz:
# Ha az "NI"-ket az 1. feladatban pl. "2200.01.01"-re cseréltük volna, akkor
# itt az ilyen dátumú filmeket ki kellene hagyni, hiszen ez egy szerdai nap, így ha a
# felhasználó "sze"-t ad meg, akkor ezek a filmek is beszámításra kerülnének.

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

    for cím in summa:
        ff.write(f"{cím} {summa[cím][0]} {summa[cím][1]}\n")

#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben
