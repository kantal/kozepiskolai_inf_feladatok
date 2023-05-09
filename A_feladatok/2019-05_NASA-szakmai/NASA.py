#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# NASA.py
# ÁGAZATI érettségi feladat: 2019. május, NASA
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2019

#--- 1-3. feladat ---
class Kérés:
    def __init__(self,s):

        self.Cím, self.DátumIdő, self.Get, többi= s.split("*")
        self.HttpKód, self.Méret = többi.split()
        self.bytes= self.ByteMéret()

    def ByteMéret(self):    # 6. feladat
        return 0 if self.Méret=="-" else int(self.Méret)

    def Domain(self):       # 7. feladat
        return self.Cím[-1].isalpha()

#--- 4. feladat ---
kérések=[]
összes_küldött=0    # 6. feladat
domainek= 0         # 8. feladat
httpcodes={}        # szótár a 9. feladathoz
with open("NASAlog.txt") as ff:
    for line in ff:
        line=line.strip()
        if not line:
            continue
        kk= Kérés(line)
        kérések.append(kk)
        összes_küldött+= kk.bytes
        if kk.Domain():
            domainek+=1
        httpcodes[kk.HttpKód]= httpcodes.get(kk.HttpKód,0)+1

#--- 5. feladat ---
print(f"5.feladat: Kérések száma: {len(kérések)}")

#--- 6. feladat ---
print(f"6. feladat: Válaszok összes mérete: {összes_küldött} byte")

#--- 8. feladat ---
print(f"8. feladat: Domain-es kérések: {100*domainek/len(kérések):.2f} %")

#--- 9. feladat ---
print("9. feladat: Statisztika:")
for kód,db in httpcodes.items():
    print(f"\t{kód}: {db} db")

#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben

