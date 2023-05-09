#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# extra_fejvagyiras.py
# A 2015. októberi érettségi feladat alapján, Fej vagy írás
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2016

import random
random.seed()

#--- 1. feladat ---
print("\n1. feladat")
print("A pénzfeldobás eredménye:",random.choice("IF") )

#--- 2. feladat ---
print("\n2. feladat")
írásminta=list("IiÍí")
fejminta=list("Ff")
tipp=input("Tippeljen! (F/I)= ").strip()
if tipp in írásminta:
	tipp="I"
elif tipp in fejminta:
	tipp="F"
else:
	print("Hibás tipp!")
	exit(1)

dobás= random.choice("IF")
print("A tipp {}, a dobás eredménye {} volt.".format(tipp,dobás) )
print("Ön eltalálta." if dobás==tipp else "Ön nem találta el.")

#--- 3. feladat ---
print("\n3. feladat")
dobások=0
fejek=0
with open("kiserlet.txt") as ff:
	for sor in ff:
		sor=sor.strip()
		if sor in írásminta:
			dobások+=1
		elif sor in fejminta:
			dobások+=1
			fejek+=1

print("A kísérlet {} dobásból állt.".format(dobások) )

#--- 4. feladat ---
print("\n4. feladat")
print("A kísérlet során a fej relatív gyakorisága {0:.2f}% volt.".format(fejek/dobások*100) )

#--- 5. feladat ---
print("\n5. feladat")
fejszám=0
sorozatok=0
with open("kiserlet.txt") as ff:
	for sor in ff:
		sor=sor.strip()
		if sor in fejminta:
			fejszám+=1
		elif sor in írásminta:
			if fejszám==2:
				sorozatok+=1
			fejszám=0

if fejszám==2:
	sorozatok+=1

print("A kísérlet során {} alkalommal dobtak pontosan két fejet egymás után.".format(sorozatok))

#--- 6. feladat ---
print("\n6. feladat")
hossz=0
kezdet=None		# a leghosszabb fejsorozat kezdő indexe
kezdőfej=None	# az éppen számolt fejsorozat kezdő indexe
fejszám=0
with open("kiserlet.txt") as ff:
	for index,sor in enumerate(ff):
		sor=sor.strip()
		if sor in fejminta:
			fejszám+=1
			if fejszám==1:
				kezdőfej=index
		elif sor in írásminta:
			if hossz< fejszám:
				hossz, kezdet = fejszám, kezdőfej
			fejszám=0

if hossz<fejszám:
	hossz, kezdet = fejszám, kezdőfej

print("A leghosszabb tisztafej sorozat {} tagból áll, kezdete a(z) {}. sor.".format( hossz,kezdet+1))

#--- 7. feladat ---
print("\n7. feladat")
négyesek=[]
dnégy=dict()
for i in range(1000):
	eset=""
	for k in range(4):
		eset+= random.choice("FI")
	négyesek.append(eset)
	dnégy[eset]= dnégy.get(eset,0)+1

with open("dobasok.txt","w") as ff:
	ff.write("FFFF: {}, FFFI: {}\n".format(dnégy["FFFF"],dnégy["FFFI"]))
	for eset in négyesek:
		ff.write( eset+" ")

def hasonlítandó( eset_darab):
	eset,darab= eset_darab
	return eset

rendnégy=sorted( dnégy.items(), key= hasonlítandó)
#rendnégy=sorted( dnégy.items(), key= lambda eset_db: eset_db[0] )

for eset in rendnégy:
	print(eset[0]+": ",eset[1])

#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben

