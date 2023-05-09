#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# sorozatok_extra2.py
# Érettségi feladat: 2020. október, Sorozatok
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2020

import datetime as dt

class Sorozatok:

    def __init__(self,fname):
        #--- 1. feladat ---
        self.sorozatok=[]

        with open(fname) as ff:

            l=[] # [ datetime(2017,07,16)/NI, Games, 7x01, 60, 1/0 ]
            self.dátumos=0
            self.megnézett=0
            self.időtöltés=0 # percek
            for sorszám,sor in enumerate(ff):

                sor= sor.strip()
                l.append(sor)

                if sorszám%5 == 4:

                    self.sorozatok.append(l)
                    if l[0]!="NI":
                        self.dátumos+= 1
                        l[0]= dt.datetime.strptime(l[0],"%Y.%m.%d")

                    if l[-1]=="1":
                        self.megnézett+= 1
                        self.időtöltés+= int(l[-2])

                    l=[]

            self.hét_napja=["h","k","sze","cs","p","szo","v"]


    def dátumos_epizódok(self):
        #--- 2. feladat ---
        print(f"2.feladat\nA listában {self.dátumos} db vetítési dátummal rendelkező epizód van.\n")

    def megnézett_epizódok(self):
        #--- 3. feladat ---
        print(f"3. feladat\nA listában lévő epizódok {self.megnézett/len(self.sorozatok):.2%}%-át látta.\n")

    def eltöltött_idő(self):
        #--- 4. feladat ---
        tidő= dt.timedelta(minutes=self.időtöltés)
        print(f"4. feladat\nSorozatnézéssel {tidő.days} napot {tidő.seconds//3600} órát és {tidő.seconds%3600//60} percet töltött.\n")


    def eddig_megnézett(self, megadott_dátum=None):
        #--- 5. feladat ---
        print("5. feladat")
        if not megadott_dátum:
            megadott_dátum= input("Adjon meg egy dátumot (éééé.hh.nn)! Dátum= ")
        else:
            print(megadott_dátum)

        megadott_dátum= dt.datetime.strptime(megadott_dátum.strip(),"%Y.%m.%d")

        for dátum,cím,epizód,perc,megtekintett in self.sorozatok:

            if dátum=="NI":
                continue
            if megadott_dátum >= dátum and megtekintett=="0":
                print(f"{epizód}\t{cím}")
        print()


    def adott_napokon_játszott(self, megadott_nap=None):
        #--- 7. feladat ---
        print("7. feladat")
        if not megadott_nap:
            megadott_nap= input("Adja meg a hét egy napját (például cs)! Nap= ")
        else:
            print(megadott_nap)

        megadott_nap= megadott_nap.strip()

        adott_napon= set()

        for dátum,cím,epizód,perc,megtekintett in self.sorozatok:

            if dátum=="NI":
                continue
            if megadott_nap == self.hét_napja[dátum.isoweekday()-1]:
                adott_napon.add(cím)

        if not adott_napon:
            print("Az adott napon nem kerül adásba sorozat.")
        else:
            print(*adott_napon, sep="\n")


    def szumma(self,fname="summa.txt"):
        #--- 8. feladat ---
        summa= dict()   # cím --> [percek,epizódok_száma]
        for dátum,cím,epizód,perc,megtekintett in self.sorozatok:

            perc= int(perc)
            if cím not in summa:
                summa[cím]= [perc,1]
            else:
                summa[cím][0]+= perc
                summa[cím][1]+= 1

        with open(fname,"w") as ff:

            for cím,(perc,db) in summa.items():
                ff.write(f"{cím} {perc} {db}\n")

#--
S= Sorozatok("lista.txt")
S.dátumos_epizódok()
S.megnézett_epizódok()
S.eltöltött_idő()
S.eddig_megnézett()
#S.eddig_megnézett("2017.10.18")
S.adott_napokon_játszott()
#S.adott_napokon_játszott("cs")
S.szumma()
#S.szumma("summa1.txt")

#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben
