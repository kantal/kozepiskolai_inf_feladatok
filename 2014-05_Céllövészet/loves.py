#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# loves.py,
# Érettségi feladat: 2014. május, Céllövészet
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2016

#--- 1. feladat ---
#print("\n1. feladat")
verseny=[]
with open("verseny.txt") as ff:
	next(ff)	# Az adatfájl első sorára, azaz a versenyzők számának feldolgozására nincs szükségünk.
	for sor in ff:
		verseny.append(sor.strip())
	
#--- 2. feladat ---
print("\n2. feladat")	
print("Az egymást követően többször találó versenyzők:",end=" ")
for index,találatok in enumerate(verseny):
	if "++" in találatok:
		print(index+1,end=" ")
print()		

#--- 3. feladat ---
print("\n3. feladat")
rajtszám=None
legtöbb=0
for index,találatok in enumerate(verseny):
	if len(találatok)>legtöbb:
		legtöbb= len(találatok)
		rajtszám= index+1
print("A legtöbb lövést leadó versenyző rajtszáma: ",rajtszám)

#--- 4. feladat ---
#print("\n4. feladat")
#Függvény loertek(sor:karaktersorozat):egész szám
#	aktpont:=20
#	ertek:=0
#	Ciklus i:=1-től hossz(sor)-ig
#		Ha aktpont>0 és sor[i]=”-” akkor
#			aktpont:=aktpont-1
#		Különben
#			ertek:=ertek+aktpont
#		Elágazás vége
#	Ciklus vége
#	loertek:=ertek
#Függvény vége
def loertek(sor):
	aktpont=20
	ertek=0
	for i in range(len(sor)):
		if aktpont>0 and sor[i]=="-":
			aktpont-=1
		else:
			ertek+=aktpont
	return ertek
		
#--- 5. feladat ---
print("\n5. feladat")
megadott_rajtszám= int( input("Adjon meg egy rajtszámot! " ))
#if megadott_rajtszám<1 or megadott_rajtszám>len(verseny):
#	print("Hibás rajtszám!")
#	exit(1)
	
print("5a. feladat: Célt érő lövések:",end=" ")
sorozat= verseny[megadott_rajtszám-1]
találatok=0
for index,találat in enumerate(sorozat):
	if találat=="+":
		print(index+1,end=" ")
		találatok+=1
print()		
print("5b. feladat: Az eltalált korongok száma:", találatok)

hibátlanok=sorozat.split("-")
print("5c. feladat: A leghosszabb hibátlan sorozat hossza:", len(max(hibátlanok)) )

print("5d. feladat: A versenyző pontszáma:", loertek(sorozat))

#--- 6. feladat ---
#print("\n6. feladat")
sorrend= [ (index+1, loertek(sorozat)) for index,sorozat in enumerate(verseny) ] #(rajtszám,pontszám)

def hasonlítandó( rajtszám_pontszám):
	return rajtszám_pontszám[1]

sorrend.sort(reverse=True, key= hasonlítandó)
#sorrend.sort(reverse=True, key= lambda rajtszám_pontszám: rajtszám_pontszám[1])

#print(sorrend)

with open("sorrend.txt","w") as ff:
	ff.write("1\t{}\t{}\n".format(sorrend[0][0],sorrend[0][1]) )
	helyezés=1
	for index in range(1,len(sorrend)):
		if sorrend[index][1] != sorrend[index-1][1]:
			helyezés= index+1
		ff.write("{}\t{}\t{}\n".format( helyezés,sorrend[index][0],sorrend[index][1]) )

#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben


