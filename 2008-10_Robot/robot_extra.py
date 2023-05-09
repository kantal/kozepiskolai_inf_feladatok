#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# robot_extra.py
# Érettségi feladat: 2008. október, Robot
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2018

import math     # sqrt

#--- 1. feladat ---
print("\n1. feladat: Az adatok beolvasása.")
programok=[]
with open("program.txt") as ff:
    ff.readline()    # A fájl első sorát beolvassuk, de nincs rá szükségünk.
    programok=[ sor.strip() for sor in ff ]  # A második sortól folytatódik a beolvasás.

#--- 2. feladat ---
print("\n2. feladat")
#--- 2a. ---
sorszám= int(input("Kérem az utasítás sorszámát (1-{}):".format(len(programok))) )
sor= programok[sorszám-1]
print(sor)
for minta in ("ED","DE","KN","NK"):
    if minta in sor:
        print("egyszerűsíthető")
        break
else:   # A 'for'-hoz tartozik; akkor hajtódik végre, ha nem volt a ciklusban 'break'.
    print("nem egyszerűsíthető")

#--- 2b.,2c. ---
x,y,maxtáv2,lépészám=0,0,0,0
mozgás={"E":(1,0),"D":(-1,0),"K":(0,1),"N":(0,-1)}  # Kiegészíthetnénk pl. az ÉNy-i iránnyal: "Q":(1,-1)

for index,irány in enumerate(sor):

    dy,dx=  mozgás[irány]
    y+= dy
    x+= dx

    táv2= x*x+y*y
    if táv2 > maxtáv2:
        lépésszám= index+1
        maxtáv2= táv2

print("{} lépést kell tenni az ED, {} lépést a KN tengely mentén.".format(abs(y),abs(x)))
print( lépésszám, round(math.sqrt(maxtáv2),3) )

#--- 3. feladat ---
print("\n3. feladat")

for progindex,sor in enumerate(programok):

    fogyasztás=2 +len(sor)
    for index in range(1,len(sor)):
        if sor[index]!=sor[index-1]:
            fogyasztás+=2

    if fogyasztás<=100:
        print(progindex+1,fogyasztás)

#--- 4. feladat ---
print("\n4. feladat: az új programok kiírása")

with open("ujprog.txt","w") as ff:

    for prog in programok:
        db=[1]
        irány=[ prog[0] ]
        for index in range(1,len(prog)):
            if prog[index]==irány[-1]:
                db[-1]+=1
            else:
                irány.append( prog[index] )
                db.append(1)

        for index in range(len(irány)):
            if db[index]>1:
                ff.write( str(db[index]) )
            ff.write( irány[index] )
            
        ff.write("\n") 


#--- 5. feladat ---
újformátum= input("\n5. feladat: Adjon meg egy új formátumú programot: ")
szám=0
for karakter in újformátum:
    if karakter.isdigit():
        szám= 10*szám +int(karakter)
    else:
        print(karakter if szám==0 else szám*karakter, end="")
        szám=0

print()

#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben


