#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# hianyzasok_extra.py
# Érettségi feladat: 2017. október, Hiányzások
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2017

#--- 4. feladat ---

def  hetnapja(honap, nap):
    """ A hét napjának nevét adja meg a feladat tárgyát képező évben.

        honap= 1-12; nap= 1-28/30/31
        A feladat kiírása szerint:
            - az adott év nem szökőév;
            - január 1. hétfő volt;
            - a bemeneti értékek mindig helyesek (pl. nem lesz ilyen: honap=2, nap=30);
    """
    napnev= ("vasarnap", "hetfo", "kedd", "szerda", "csutortok", "pentek", "szombat")
    napszam= (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 335)
    napsorszam= (napszam[honap-1]+nap) % 7
    return napnev[napsorszam]


#--- 1. feladat ---
#print("\n1. feladat: Az adatok beolvasása")
napló=[]
with open("naplo.txt") as ff:

    napi_adat=[]
    for sor in ff:
        t1,t2,t3= sor.split()   # "# hónap nap" vagy "vnév knév tanórák"
        if t1=="#":             # "# hónap nap"
            if napi_adat:
                napló.append(napi_adat)
                napi_adat=[]
            hónap= int(t2)
            nap= int(t3)
            napi_adat.append( (hónap, nap, hetnapja(hónap,nap)) )
        else:                   # "vnév knév tanórák"
            napi_adat.append( (t1+" "+t2, t3) )

    napló.append(napi_adat)
    #print(napló)     # szemrevételezés

#--- 2. feladat ---
print("\n2. feladat")
bejegyzések_száma=0
# A "dátum"-ot leválasztva, a tétel maradékából egy listát képezünk a "*bejegyzések" kifejezéssel.
for dátum, *bejegyzések in napló:
    bejegyzések_száma+= len(bejegyzések)

print("A naplóban {} bejegyzés van.".format(bejegyzések_száma))

#--- 3. feladat ---
print("\n3. feladat")
igazolt,igazolatlan=0,0
for dátum, *bejegyzések in napló:
    for név,tanórák in bejegyzések:
        igazolt+= tanórák.count("X")
        igazolatlan+= tanórák.count("I")

print("Az igazolt hiányzások száma {}, az igazolatlanoké {} óra.".format(igazolt,igazolatlan))

#--- 5. feladat ---
print("\n5. feladat")
hónap= int(input("A hónap sorszáma="))
nap= int(input("A nap sorszáma="))

print("Azon a napon {} volt.".format(hetnapja(hónap,nap)))

#--- 6. feladat ---
print("\n6. feladat")
transtbl= str.maketrans( {"á":"a","é":"e","ő":"o","ü":"u","ö":"o"} ) # majd ékezetes napneveket is megadhatunk
napnév= input("A nap neve=").strip().lower().translate(transtbl)
óra= int(input("Az óra sorszáma="))
hiányzások=0
for dátum, *bejegyzések in napló:
    if dátum[2]==napnév:
        for név,tanórák in bejegyzések:
            if tanórák[óra-1] in ("I","X"):
                hiányzások+= 1

print("Ekkor összesen {} óra hiányzás történt.".format(hiányzások))

#--- 7. feladat ---
print("\n7. feladat")
hiányzók={}
for dátum, *bejegyzések in napló:
    for név,tanórák in bejegyzések:
        hiányzók[név]= hiányzók.get(név,0)+tanórák.count("I")+tanórák.count("X")

hiányzók= sorted(hiányzók.items(), reverse=True, key=lambda t: t[1] )

egy_név, legtöbb= hiányzók[0]
print("A legtöbbet hiányzó tanulók:", end=" ")

for név,óraszám in hiányzók:
    if legtöbb!=óraszám:
        break
    print(név,end=" ")
print()


#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben

