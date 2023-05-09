#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# tesztverseny.py
# Érettségi feladat: 2017. május, Tesztverseny
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2017


#--- 1. feladat ---
print("\n1. feladat: Az adatok beolvasása")

with open("valaszok.txt") as ff:
    
    megoldások= next(ff).strip()
    eredmények= []
    for sor in ff:
        eredmények.append( sor.split() )    # [ [személyi_kód, a_személy_válaszai], ... ]


#--- 2. feladat ---
print("\n2. feladat: A vetélkedőn {} versenyző indult.".format(len(eredmények)))

    	
#--- 3. feladat ---
bekért_kód= input("\n3. feladat: A versenyző azonosítója = ").strip()
bekért_válasza= None

for szkód,szválaszok in eredmények:
    if bekért_kód == szkód:
        bekért_válasza= szválaszok
        break
    
print("{}  (a versenyző válasza)".format(bekért_válasza))


#--- 4. feladat ---
print("\n4. feladat:")
print("{}\t(a helyes megoldás)".format(megoldások))
helyesek=""
for index,jel in enumerate(megoldások):
    helyesek+= "+" if jel==bekért_válasza[index] else " "
    
print("{}\t(a versenyző helyes válaszai)".format(helyesek))


#--- 5. feladat ---
fsorszám= int(input("\n5. feladat: A feladat sorszáma = "))-1
jó_válaszok=0
jó_jel= megoldások[fsorszám]
for szkód,szválaszok in eredmények:
    if szválaszok[fsorszám] == jó_jel:
        jó_válaszok+=1

print("A feladatra {} fő, a versenyzők {}%-a adott helyes választ.".format(jó_válaszok,round(jó_válaszok*100/len(eredmények),2) ) ) 


#--- 6. feladat ---
print("\n4. feladat: A versenyzők pontszámának meghatározása")

def fpontos(megoldások,szválaszok):
    #     1,2,3,4,5,6,7,8,9,0,1,2,3,4
    pont=[3,3,3,3,3,4,4,4,4,4,5,5,5,6]
    szumma=0
    for index,jel in enumerate(megoldások):
        if jel==szválaszok[index]:
            szumma+=pont[index]
    return szumma

with open("pontok.txt","w") as ff:

    for index, (szkód,szválaszok) in enumerate(eredmények):

        pontszám= fpontos(megoldások,szválaszok)
        ff.write("{} {}\n".format(szkód,pontszám))
        # A pontszámokat egyben csatoljuk az eredményekhez is:
        eredmények[index].append(pontszám)      # [ [személyi_kód, a_személy_válaszai, pontszám], ... ]


#--- 7. feladat ---
print("\n7. feladat: A verseny legjobbjai:")
def hasonlítandó( adat ):
    szkód,szválaszok,pontszám = adat
    return pontszám

eredmények.sort(key= hasonlítandó, reverse=True)
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

