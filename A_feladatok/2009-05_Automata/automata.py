#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# automata.py
# Érettségi feladat: 2009. május, Automata
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2016

#--- 1. feladat ---
print("\n1. feladat")
automata=[]
with open("csoki.txt") as ff:
	rekeszek_száma= int(next(ff))
	for sor in ff:
		rekeszszám, db, ár = sor.split()
		automata.append( [int(rekeszszám),int(db),int(ár)])
		
vásárlások=[]
with open("vasarlas.txt") as ff:
	vásárlások_száma= int(next(ff))
	for sor in ff:
		s=sor.split()
		rekeszszám,db,érmék = s[0],s[1],s[2:]	#  rekeszszám,db, [f1,f2,f5,f10,f20,f50,f100]
		#rekeszszám,db, *érmék = sor.split()			
		
		vásárlások.append( [int(rekeszszám), int(db), [int(e) for e in érmék] ] )
		
#--- 2. feladat ---
print("\n2. feladat")
összeg=0
for rekeszszám,db,ár in automata:
	összeg+= ár*db
	
print("Az automatában", összeg, "fabatka értékű csokoládé van.")

#--- 3. feladat ---
print("\n3. feladat")

#kiválasztottak=set()
#for rekeszszám,db,érmék in vásárlások:
#	kiválasztottak.add( rekeszszám)

kiválasztottak={ rek for rek,db,érmék in vásárlások} 	

print("A kiválasztott rekeszek:",end=' ')
for rek in kiválasztottak:
	print(rek,end=' ')
print()	

#--- 4. feladat ---
pénzkeret=int(input("\n4. feladat Kérem a pénzösszeget! "))
választhatók=[]
for rekeszszám,db,ár in automata:
	if db >= 7  and  pénzkeret >= 7*ár:
		választhatók.append(rekeszszám)

print("A választható rekeszek:",end=' ')
for rek in választhatók:
	print(rek,end=' ')
print()
			
#--- 5. feladat ---
print("\n5. feladat")
reksorszám=int(input("Adja meg egy rekesz sorszámát (1-{}): ".format(rekeszek_száma)))
darabszám=int(input("Adja meg a darabszámot: "))

rekeszszám, db, ár = automata[reksorszám-1]
# ár= automata[reksorszám-1][2]
összeg= darabszám*ár

csökk_címletek= [100,50,20,10,5,2,1]
érmék= [ 0 for i in range(len(csökk_címletek)) ]

# A feladat kiírása szerinti algoritmus, amely a megadott adatokkal jól kell hogy működjön (egyébként nem biztos):
while összeg:
	for index,címlet in enumerate(csökk_címletek):
		if címlet<=összeg:
			érmék[index]+= 1;
			összeg-= címlet
			break

for index,érme in enumerate(érmék):
	if érme:
		print(csökk_címletek[index],érme)
print()		

#--- 6. feladat ---
print("\n6. feladat")

címletek= [1,2,5,10,20,50,100]

def befizetés( érmék):
	totál=0
	for index,címlet in enumerate(címletek):
		totál+= címlet*érmék[index]
	return totál

rekesz,csokiszám,egységár = automata[6]

with open("rekesz7.txt","w") as ff:
	for index,tétel in enumerate(vásárlások):
		rekszám,db,érmék= tétel
		if rekszám!=7:
			continue
		if db > csokiszám:
			ff.write("{}\tkevés a csoki\n".format(index+1))
		elif befizetés(érmék) < db*egységár:
			ff.write("{}\tnem volt elég pénz\n".format(index+1))
		else:
			ff.write("{}\t{}\n".format(index+1,db))
			csokiszám-= db

		
#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben


