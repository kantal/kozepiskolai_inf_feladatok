#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# eutazas.py
# Érettségi feladat: 2019. november, eUtazás
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2019


#--- 1. feladat ---
# 0 20190326-0700 4170861 NYB 20190404
# 0 20190326-0700 9031038 JGY 3
adatok=[]
érvénytelen=0
felszállók= 30*[0]
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

        felszállók[int(megálló)]+= 1

            
#--- 2. feladat ---
print(f"2. feladat\nA buszra {len(adatok)} utas akart felszállni.")

#--- 3. feladat ---
print(f"3. feladat\nA buszra {érvénytelen} utas nem szállhatott fel.")

#--- 4. feladat ---
legtöbb=max(felszállók)
hely= felszállók.index(legtöbb)
print(f"4. feladat\nA legtöbb utas ({legtöbb} fő) a {hely}. megállóban próbált felszállni.")

#--- 5. feladat ---
print(f"5. feladat\nIngyenesen utazók száma: {db_ingy} fő\nA kedvezményesen utazók száma: {db_kedv} fő")

#--- 6. feladat ---
def napokszama(e1,h1,n1,e2,h2,n2):
    h1 = (h1 + 9) % 12
    e1 = e1 - h1 // 10
    d1= 365*e1 + e1 // 4 - e1 // 100 + e1 // 400 + (h1*306 + 5) // 10 + n1 - 1
    h2 = (h2 + 9) % 12
    e2 = e2 - h2 // 10
    d2= 365*e2 + e2 // 4 - e2 // 100 + e2 // 400 + (h2*306 + 5) // 10 + n2 - 1
    return d2-d1

#--- 7. feladat ---
with open("figyelmeztetes.txt","w") as ff:
    
    for megálló,dátum,idő,bszám,típus,lejárat in adatok:

        if típus!="JGY" and lejárat>=dátum:
            
            e1,h1,n1= int(dátum[:4]), int(dátum[4:6]), int(dátum[6:])
            e2,h2,n2= int(lejárat[:4]), int(lejárat[4:6]), int(lejárat[6:])
            if napokszama(e1,h1,n1,e2,h2,n2)<=3:
                
                s=f"{bszám} {e2}-{h2:02}-{n2:02}\n"
                ff.write(s)

#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben

