#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# tesztverseny_extra.py
# Érettségi feladat: 2017. május, Tesztverseny
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2017

# A teszteléshez módosítsuk a válaszok2.txt fájlt!

import sys

#--- 1. feladat ---
print("\n1. feladat: Az adatok beolvasása")

def helyes_betűk(betűsor, helyesek):

    for betű in betűsor:
        if betű not in helyesek:
            return False
    return True


with open("valaszok2.txt") as ff:   

    eredmények=[]
    
    megoldások=""
    while not megoldások:       
        megoldások= next(ff).strip()
        if not megoldások:          # az üres sorokat átugorjuk
            continue
        if megoldások[0]=="#":      # kommentnek vesszük a '#' jellel kezdődő sorokat
            megoldások=""
        
    if not helyes_betűk(megoldások,"ABCD"):    # a megoldókulcsban csak ezek a betűk lehetnek
        print("Nem jó betűk a megoldókulcsban!",megoldások)
        sys.exit(1)
    
    for sor in ff:

        sor= sor.strip()
        if not sor or sor[0]=="#":  # az üres sorokat és a kommenteket átugorjuk
            continue
        szk_szv= sor.split()    # ezt várjuk: [személyi_kód, a_személy_válaszai]
        if len(szk_szv)!=2:
            print("Nem megfelelő számú adat!", sor)
            sys.exit(1)

        if len(szk_szv[1]) != len(megoldások):
            print("Nem megfelelő hosszúságú válasz!", sor)
            sys.exit(1)
        if not helyes_betűk(szk_szv[1],"ABCDX"):    
            print("Nem jó betűk!", sor)
            sys.exit(1)
            
        eredmények.append( szk_szv )    # [ [személyi_kód, a_személy_válaszai], ... ]

    # Vannak-e duplikált azonosítók?
    kódlista= [ szkód for szkód,szválaszok in eredmények ]
    kódkészlet= set(kódlista)
    if len(kódkészlet) != len(kódlista):
        for szkód in kódkészlet:
            kódlista.remove(szkód)
        print("Duplikált azonosító!", kódlista)
        sys.exit(1)


#--- 2. feladat ---
print("\n2. feladat: A vetélkedőn {} versenyző indult.".format(len(eredmények)))

        
#--- 3. feladat ---
bekért_kód= input("\n3. feladat: A versenyző azonosítója = ").strip()
bekért_válasza= None

for szkód,szválaszok in eredmények:
    
    if bekért_kód == szkód:
        bekért_válasza= szválaszok
        break
else:           # az 'else' a 'for'-hoz tartozik
    print("Nincs ilyen kódú versenyző!")
    sys.exit(1)
    
print("{}  (a versenyző válasza)".format(bekért_válasza))


#--- 4. feladat ---
print("\n4. feladat:")
print("{}\t(a helyes megoldás)".format(megoldások))
helyesek=""
for index,jel in enumerate(megoldások):
    helyesek+= "+" if jel==bekért_válasza[index] else " "
    
print("{}\t(a versenyző helyes válaszai)".format(helyesek))


#--- 5. feladat ---
fsorszám= int(input("\n5. feladat: A feladat sorszáma ({}-{}) = ".format(1,len(megoldások)) ))
if fsorszám <1 or fsorszám>len(megoldások):
    print("Hibás feladatsorszám!")
    sys.exit(1)
fsorszám-=1
jó_válaszok=0
jó_jel= megoldások[fsorszám]
for szkód,szválaszok in eredmények:
    if szválaszok[fsorszám] == jó_jel:
        jó_válaszok+=1

print("A feladatra {} fő, a versenyzők {}%-a adott helyes választ.".format(jó_válaszok,round(jó_válaszok*100/len(eredmények),2) ) ) 

#--- 6. feladat ---
print("\n4. feladat: A versenyzők pontszámának meghatározása")

def fpontos(megoldások,szválaszok):

    pont= 5*[3] + (10-6+1)*[4] + (13-11+1)*[5] + [6]
    szumma=0
    for index,jel in enumerate(megoldások):
        if jel==szválaszok[index]:
            szumma+=pont[index]
    return szumma

with open("pontok2.txt","w") as ff:

    for index, (szkód,szválaszok) in enumerate(eredmények):

        pontszám= fpontos(megoldások,szválaszok)
        ff.write("{} {}\n".format(szkód,pontszám))
        # A pontszámokat egyben csatoljuk az eredményekhez is:
        eredmények[index].append(pontszám)      # [ [személyi_kód, a_személy_válaszai, pontszám], ... ]


#--- 7. feladat ---
print("\n7. feladat: A verseny legjobbjai:")

eredmények.sort(key= lambda adat: adat[2], reverse=True)
díj=1
előzőpsz= eredmények[0][2]
for szkód,szválaszok,pontszám in eredmények:
    if pontszám < előzőpsz:
        díj+=1
        előzőpsz= pontszám
    if díj > 3:
        break
    print("{}. díj ({} pont): {}" .format(díj,pontszám,szkód))


#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben

