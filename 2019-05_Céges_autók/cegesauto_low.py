#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# cegesauto_low.py
# Érettségi feladat: 2019. május, Céges autó
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2019
""" Példa egy alacsony szintű programozási nyelven megvalósítható, nem igazán "pythonos" megoldásra.
A listát rögzített méretű tömbként kezeljük, és az indexelésen kívül nem használunk más
listaműveletet. Erősen kihasználjuk a feladatban megadott értékeket: a tételek maximális számát,
az autók számát, a rendszámok és a személyi azonosítók formátumát és számozását. Ezek megváltozása
esetén a programot módosítani szükséges, ami nem biztos, hogy egyszerű feladat; gondoljunk csak arra, 
ha a megadott rendszámokat ki kellene egészíteni ilyenekkel: CEG-007, KFT-111.
"""
#--- 1. feladat ---
MAXNtétel= 500
Nautó=10
ki,be="0","1"

def str2autoid(s):  # kihasználjuk a rsz formátumát és számozását
    return int(s[3:])-300
    
def autoid2str(n):  # kihasználjuk a rsz formátumát és számozását
    return "CEG"+str(n+300)    
    
adatok= MAXNtétel*[None]
utolsó_elvitel=None         # a 2. feladathoz
kibe= Nautó*[0]             # a 4. feladathoz

kezdőkm= Nautó*[None]       # az 5. feladathoz
utolsókm= Nautó*[None]      # az 5. feladathoz

szakasz_út=0                 # a 6. feladathoz
szakasz_szem=None            # a 6. feladathoz
szakasz_kmóra=Nautó*[None]   # a 6. feladathoz

Ntétel=0

with open("autok.txt") as ff:
    for line in ff:
        line=line.strip()
        if not line:    # üres sor
            continue
        # 1 08:45 CEG306 501 23989 0
        nap,óópp,rsz,szem,km,irány= line.split()
        km,aid= int(km),str2autoid(rsz)
        adatok[Ntétel]= (nap,óópp,aid,szem,km,irány)
        Ntétel+=1
        # A 2. feladathoz:
        if irány==ki:    # kihajtás
            utolsó_elvitel= (nap,rsz)

        # A 4. feladathoz:
        kibe[aid]+=1

        # Az 5. feladathoz
        if kezdőkm[aid]==None:
            kezdőkm[aid]=km
        elif irány==be:  # behajtás
            utolsókm[aid]=km
        
        # A 6. feladathoz
        if szakasz_kmóra[aid]==None:
            szakasz_kmóra[aid]= km
        elif irány==be:              # behajtás
            újtáv= km-szakasz_kmóra[aid]
            if újtáv > szakasz_út:
                szakasz_út= újtáv
                szakasz_szem= szem
            szakasz_kmóra[aid]= km
            
#--- 2. feladat ---
nap,rsz= utolsó_elvitel    
print( f"2. feladat\n{nap}. nap rendszám: {rsz}")

#--- 3. feladat ---
kért_nap= input("3. feladat\nNap: ").strip()
print(f"Forgalom a(z) {kért_nap}. napon:")

for i in range(Ntétel):
    nap,óópp,aid,szem,km,irány= adatok[i]
    if nap==kért_nap:
        print(f"{óópp} {autoid2str(aid)} {szem} {'ki' if irány==ki else 'be'}")

#--- 4. feladat ---
db=0
for i in range(Nautó):
    if kibe[i]%2:
        db+=1
                
print(f"4. feladat\nA hónap végén {db} autót nem hoztak vissza.")

#--- 5. feladat ---
print("5. feladat")
for i in range(Nautó):
    if utolsókm[i]:
        print(f"{autoid2str(i)} {utolsókm[i]-kezdőkm[i]} km")
    else:
        print(f"{autoid2str(i)} 0 km")

#--- 6. feladat ---
print(f"6. feladat\nLeghosszabb út: {szakasz_út} km, személy: {szakasz_szem}")

#--- 7. feladat ---
print("7. feladat")
rendszám= input("Rendszám: ").strip().upper()
megadott_aid= str2autoid(rendszám)
fájlnév=f"{rendszám}_menetlevel_low.txt"

with open(fájlnév,"w") as ff:

    for i in range(Ntétel):
        nap,óópp,aid,szem,kmóra,irány= adatok[i]
        if megadott_aid==aid:
            if irány==ki:
                ff.write(f"{szem}\t{nap}. {óópp}\t{kmóra} km")
            else:
                ff.write(f"\t{nap}. {óópp}\t{kmóra} km\n")

print("Menetlevél kész.")
#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben

