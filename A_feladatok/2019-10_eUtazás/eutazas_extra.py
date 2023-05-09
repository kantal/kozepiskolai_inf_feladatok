#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# eutazas_extra.py
# Érettségi feladat: 2019. november, eUtazás
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2019

import datetime as dt   # A 6. feladathoz szükséges.

#--- 1. feladat ---
# 0 20190326-0700 4170861 NYB 20190404
# 0 20190326-0700 9031038 JGY 3
adatok=[]
érvénytelen=0

# Szótárt használunk: bármennyi megálló lehet, nem csak 30. (kulcs:megálló, érték: felszálló_utasok)
felszállók= {}

b_kedvezményes=["TAB","NYB"]
b_ingyenes=["NYP","RVS","GYK"]
db_kedv,db_ingy=0,0
 
with open("utasadat.txt") as ff:

    for line in ff:
        megálló,dátum,bszám,típus,lejárat= line.split()
        dátum,idő= dátum.split("-")
        adatok.append( (megálló,dátum,idő,bszám,típus,lejárat) )

        """ Figyelem: 1) minden adat karakterlánc, és így a 0 az "0"!
         2) Mivel a nagyobb számok karakterkódja nagyobb értékű, a kisebbeké kisebb, és a
         dátumokban a hónap és a nap két karakteres, ezért a dátumok összehasonlítását
         elvégezhetjük a karakterláncaik összevetésével.
        """
        if (típus=="JGY" and lejárat=="0") or (típus!="JGY" and lejárat<dátum):
            érvénytelen+=1
        else:
            if típus in b_kedvezményes:
                db_kedv+=1
            elif típus in b_ingyenes:
                db_ingy+=1

        felszállók[megálló]= felszállók.get(megálló,0)+1    # A 'megálló' maradhatott karakterlánc.

            
#--- 2. feladat ---
print(f"2. feladat\nA buszra {len(adatok)} utas akart felszállni.")

#--- 3. feladat ---
print(f"3. feladat\nA buszra {érvénytelen} utas nem szállhatott fel.")

#--- 4. feladat ---
# A max. kiválasztáshoz a kulcs a felszállók száma, azaz az 1. indexű elem: t=(megálló, felszállók)
legtöbb=max(felszállók.items(), key=lambda t: t[1])   

print(f"4. feladat\nA legtöbb utas ({legtöbb[1]} fő) a {legtöbb[0]}. megállóban próbált felszállni.")

#--- 5. feladat ---
print(f"5. feladat\nIngyenesen utazók száma: {db_ingy} fő\nA kedvezményesen utazók száma: {db_kedv} fő")

#--- 6. feladat ---
def napokszama(dátum1,dátum2):

    return (dt.datetime.strptime(dátum2,"%Y%m%d") - dt.datetime.strptime(dátum1,"%Y%m%d")).days
    

#--- 7. feladat ---
with open("figyelmeztetes2.txt","w") as ff:     # Megváltoztattuk a fájlnevet, hogy az eredetivel össze tudjuk hasonlítani.
    
    for megálló,dátum,idő,bszám,típus,lejárat in adatok:

        if típus!="JGY" and lejárat>=dátum:
            
            if napokszama(dátum,lejárat)<=3:
                
                s=f"{bszám} {lejárat[:4]}-{lejárat[4:6]}-{lejárat[6:]}\n"
                ff.write(s)

#---------------------------------------------------------------------------
# További feladatok: http://sites.google.com/site/eutlantis/erettsegi
# Ajánlott olvasmány: www.interkonyv.hu/konyvek/koos_antal_python_a_gepben
