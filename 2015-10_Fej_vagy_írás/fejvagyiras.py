#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# fejvagyiras.py
# Érettségi feladat, 2015. október, Fej vagy írás
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2016

import random
random.seed()

#--- 1. feladat ---
print("\n1. feladat")
print("A pénzfeldobás eredménye:",random.choice("IF") )

#--- 2. feladat ---
print("\n2. feladat")
tipp=input("Tippeljen! (F/I)= ").strip()
dobás= random.choice("IF")
print("A tipp", tipp+", a dobás eredménye", dobás, "volt.")
if dobás==tipp:
	print("Ön eltalálta.")
else:
	print("Ön nem találta el.")
	
#--- 3. feladat ---
print("\n3. feladat")
dobások=0
fejek=0
with open("kiserlet.txt") as ff:
	for sor in ff:
		if sor.strip()=="I": 
			dobások+=1
		else:
			dobások+=1
			fejek+=1
	
print("A kísérlet", dobások,"dobásból állt.")

#--- 4. feladat ---
print("\n4. feladat")	
print("A kísérlet során a fej relatív gyakorisága {0:.2f}% volt.".format(fejek/dobások*100) )

#--- 5. feladat ---
print("\n5. feladat")
fejszám=0
sorozatok=0
with open("kiserlet.txt") as ff:
	for sor in ff:
		if sor.strip()=="F": 
			fejszám+=1
		else:
			if fejszám==2:
				sorozatok+=1
			fejszám=0
				
if fejszám==2:
	sorozatok+=1				

print("A kísérlet során",sorozatok,"alkalommal dobtak pontosan két fejet egymás után.")

#--- 6. feladat ---
print("\n6. feladat")
hossz=0
kezdet=None
fejszám=0
with open("kiserlet.txt") as ff:
	for index,sor in enumerate(ff):
		if sor.strip()=="F": 
			fejszám+=1
		else:
			if hossz< fejszám:
				hossz, kezdet = fejszám, index-fejszám
			fejszám=0
				
if hossz<fejszám:
	hossz, kezdet = fejszám, index-fejszám

print("A leghosszabb tisztafej sorozat {} tagból áll, kezdete a(z) {}. dobás.".format( hossz,kezdet+1))

#--- 7. feladat ---
#print("\n7. feladat")
négyesek=[]
f3f=0
f3í=0
for i in range(1000):
	eset=""
	for k in range(4):
		eset+= random.choice("FI")
	négyesek.append( eset)	
	if eset=="FFFF":
		f3f+=1
	elif eset=="FFFI":
		f3í+=1	

with open("dobasok.txt","w") as ff:
	ff.write("FFFF: {}, FFFI: {}\n".format(f3f,f3í))
	for eset in négyesek:
		ff.write( eset+" ")

#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben, 2. kiadás

