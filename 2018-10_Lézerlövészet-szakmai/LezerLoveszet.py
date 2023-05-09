#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# LezerLoveszet.py
# ÁGAZATI érettségi feladat: 2018. október, Lézerlövészet
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2018

import math

#--- 1-3., 6.,8. feladatok
class JátékosLövése:

    célx,cély=None,None
    
    def __init__(self,adatok,sorszám):

        self.sorszám= sorszám
        játékos,x,y= adatok.replace(",",".").split(";")
        self.játékos=játékos.strip()
        self.x, self.y= float(x), float(y)
        self.távolság= self.Távolság()
        self.pontszám= self.Pontszám()

    # 6.feladat
    def Távolság(self): 

        dx= JátékosLövése.célx - self.x
        dy= JátékosLövése.cély - self.y
        return math.sqrt(pow(dx,2) + pow(dy,2))

    # 8. feladat
    def Pontszám(self): 
        return round( max(0, 10-self.távolság), 2 )

#--- 4. feladat ---                    
Lövések=[]
with open("lovesek.txt") as ff:
    sorszám=0
    cél_adott= False
    for sor in ff:
        sor=sor.strip()
        if not sor:        # üres sor kihagyása
            continue
        if not cél_adott:   # az első nem üres sornak a cél adatait kell tartalmaznia
            célx, cély=sor.replace(",",".").split(";")
            # Beállítjuk az osztályváltozókat:
            JátékosLövése.célx, JátékosLövése.cély= float(célx),float(cély)
            cél_adott= True
        else:
            sorszám+=1
            Lövések.append( JátékosLövése(sor,sorszám) )

#--- 5. feladat ---
print("5. feladat: Lövések száma:",len(Lövések))

#--- 7. feladat ---
legpbb=min(Lövések, key=lambda lövés: lövés.távolság)
print("7. feladat: Legpontosabb lövés:\n\t{}.; {}; {}; {}; távolság: {}".format(legpbb.sorszám,legpbb.játékos,legpbb.x,legpbb.y,legpbb.távolság))

#--- 9.,10.,11. feladat ---
nullás=0
lövésszám=dict()    # játékos_neve:lövéseinek_száma

for lövés in Lövések:
    if lövés.pontszám==0:
        nullás+=1
    lövésszám[lövés.játékos]= lövésszám.get(lövés.játékos,0)+1
    
print("9. feladat: Nulla pontos lövések száma: {} db".format(nullás))
print("10. feladat: Játékosok száma:",len(lövésszám))
print("11. feladat: Lövések száma:")
for játékos,lszám in lövésszám.items():
    print("\t{} - {} db".format(játékos,lszám))

#--- 12-13. feladat ---
print("12. feladat: Átlagpontszámok:")
átlagok=[]
for játékos in lövésszám:
    átlag=0
    for lövés in Lövések:
        if lövés.játékos==játékos:
            átlag+= lövés.pontszám
    átlagok.append( (játékos,átlag/lövésszám[játékos]) )

átlagok.sort(key=lambda t: t[1], reverse=True)

for játékos,átlag in átlagok:
    print("\t{} - {}".format(játékos,átlag))

print("13. feladat: A játék nyertese:", átlagok[0][0])

#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben

