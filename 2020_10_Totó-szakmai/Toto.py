#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# Toto.py
# ÁGAZATI érettségi feladat: 2020. október, Totó, CLI
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2020

""" A feladatot a kiírás szerint Java vagy C# nyelven kellett megoldani,
    de mi most gyakorlásképpen Pythonban készítjük el.
"""

# A csharp.txt átirata Pythonban:
from python_txt import EredményElemző


class Totó:

    def __init__(self,fadat):

        self.Adat= []
        self.telitalálat= 0
        self.ttösszeg= 0
        with open(fadat) as ff:

            next(ff)    # átugorjuk a fejlécet
            for sor in ff:

                sor= sor.strip()
                if not sor:
                    continue

                év,hét,forduló,t13p1,nyeremény,eredmények= sor.split(";")
                telitalálat= int(t13p1)
                self.telitalálat+= telitalálat
                nyeremény= int(nyeremény)
                self.Adat.append([év,hét,forduló,telitalálat,nyeremény,eredmények])
                if telitalálat:
                    self.ttösszeg+= telitalálat * nyeremény


    def __len__(self):
        return len(self.Adat)

    def tt_darab(self):
        return self.telitalálat

    def tt_átlag(self):
        return(round(self.ttösszeg/len(self.Adat)))

    def max_ny(self):
        # Egy forduló adatait adja vissza listaként
        return max(self.Adat, key=lambda forduló: forduló[4])

    def min_ny(self):
        # Egy forduló adatait adja vissza listaként
        return min(self.Adat, key= lambda ford: ford[4] or float("inf"))


    def kijelez(self,forduló, komment):

        év,hét,forduló,t13p1,nyeremény,eredmények= forduló
        print( f"\t{komment}:\n\tÉv: {év}\n\tHét: {hét}.\n\tForduló: {forduló}.\n\t" \
               f"Telitalálat: {t13p1} db\n\tNyeremény: {nyeremény} Ft\n\tEredmények: {eredmények}" )


    def döntetlen_nélkül(self):

        for forduló in self.Adat:
            if EredményElemző(forduló).NemvoltDöntetlenMérkőzés():
                return True

        return False

        # ez szebb:
        # return any("X" not in forduló[-1] for forduló in self.Adat)


#--
T= Totó("toto.txt")
print("3. feladat: Fordulók száma:",len(T))
print("4. feladat: A telitalálatos szelvények száma:",T.tt_darab(),"db")
print("5. feladat: Átlag:",T.tt_átlag(),"Ft")

print("6.feladat:\n\t")
T.kijelez(T.max_ny(), "Legnagyobb")
print()
T.kijelez(T.min_ny(), "Legkisebb")

print("8. feladat:", "Volt döntetlen nélküli forduló!" if T.döntetlen_nélkül() else "Minden fordulóban volt döntetlen mérközés.")

#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben
