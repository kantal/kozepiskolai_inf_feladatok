#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# cegesauto_oop.py
# Érettségi feladat: 2019. május, Céges autó
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2019
""" A megoldás során nem használjuk ki, hogy a tételek számának mi a korlátja, sem azt, hogy az
autók rendszáma és a személyi azonosítók milyen formátumúak és hogy miként számozódnak. Ezért
ezen feltételek megváltozása esetén a programot (valószínűleg) nem kellene módosítani.
"""
#--- 1. feladat ---
class Tétel:
    # input: "1 08:45 CEG306 501 23989 0"

    def __init__(self,s):
        self.nap, self.óópp, self.rsz, self.szem, self.km, self.irány=s.split()
        self.km= int(self.km)
    def kihajtás(self):
        return True if self.irány=="0" else False
    def behajtás(self):
        return not self.kihajtás()


adatok=[]
utolsó_elvitel=None # a 2. feladathoz
kibe={}         # szótár a 4. feladathoz
menetkm={}      # szótár az 5. feladathoz
rszkmóra={}     # szótár a 6. feladathoz
szakasz_út=0    # a 6. feladathoz
szakasz_szem=None   # a 6. feladathoz

with open("autok.txt") as ff:
    for line in ff:
        line=line.strip()
        if not line:    # üres sor
            continue
        t=Tétel(line)
        adatok.append(t)
        
        # A 2. feladathoz:
        if t.kihajtás():
            utolsó_elvitel= t

        # A 4. feladathoz:  megszámoljuk minden rendszámhoz a hozzátartozó bejegyzéseket
        kibe[t.rsz]= kibe.get(t.rsz,0)+1

        # Az 5. feladathoz: minden rsz-hoz rögzítjük a legelső kmóraállást és az utolsót;
        # a rendszám lesz a kulcs, az érték pedig egy két elemű lista: [kezdő_kmóra_állás, utolsó_kmóra_állás]
        if t.rsz not in menetkm:      # A tétel az autó első használatára vonatkozik?
            menetkm[t.rsz]=[t.km,t.km]
        else:
            menetkm[t.rsz][1]=t.km

        # A 6. feladathoz: minden rsz-hoz rögzítjük a megtett utat, a személyt és az utolsó kmóraállást
        if t.rsz not in rszkmóra:
            rszkmóra[t.rsz]= t.km    # az adott rsz-ú autó első elvitele
        elif t.behajtás:             # most már elegendő csak a visszahozást ellenőrizni
            újtáv=t.km-rszkmóra[t.rsz]
            if újtáv>szakasz_út:
                szakasz_út= újtáv
                szakasz_szem= t.szem
            rszkmóra[t.rsz]= t.km         # a kmóra állását mindenképpen frissíteni kell

#--- 2. feladat ---
print( f"2. feladat\n{utolsó_elvitel.nap}. nap rendszám: {utolsó_elvitel.rsz}")

#--- 3. feladat ---
kért_nap= input("3. feladat\nNap: ").strip()
print(f"Forgalom a(z) {kért_nap}. napon:")

for t in adatok:
    if t.nap==kért_nap:
        print(f"{t.óópp} {t.rsz} {t.szem} {'ki' if t.kihajtás() else 'be'}")

#--- 4. feladat ---
db=0
for rendszám in kibe:
    if kibe[rendszám]%2:
        db+=1
                
print(f"4. feladat\nA hónap végén {db} autót nem hoztak vissza.")

#--- 5. feladat ---
print("5. feladat")

for rsz,(kezdőkm,utolsókm) in sorted(menetkm.items()): # sorba rendezzük a rendszám szerint
    print(f"{rsz} {utolsókm-kezdőkm} km")

#--- 6. feladat ---
print(f"6. feladat\nLeghosszabb út: {szakasz_út} km, személy: {szakasz_szem}")

#--- 7. feladat ---
print("7. feladat")
rendszám= input("Rendszám: ").strip().upper()
fájlnév=f"{rendszám}_menetlevel.txt"

with open(fájlnév,"w") as ff:
    
    for t in adatok:
        if rendszám==t.rsz:
            if t.kihajtás():
                ff.write(f"{t.szem}\t{t.nap}. {t.óópp}\t{t.km} km")
            else:
                ff.write(f"\t{t.nap}. {t.óópp}\t{t.km} km\n")

print("Menetlevél kész.")
#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben
