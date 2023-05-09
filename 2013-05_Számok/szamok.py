#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# szamok.py,
# Érettségi feladat: 2013. május, Számok
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2016

#--- 1. feladat ---
#print("\n1. feladat:")
adatok=[]
with open("felszam.txt") as ff:
	for kérdés in ff:
		válasz,pont,téma = next(ff).split()
		adatok.append( (kérdés.strip(), int(válasz), int(pont), téma) )

#--- 2. feladat ---
print("\n2. feladat:")
print("Az adatfájlban", len(adatok),"feladat van")

#--- 3. feladat ---
print("\n3. feladat:")
pont1,pont2,pont3=0,0,0
for kérdés,válaszérték,pontszám,téma in adatok:
	if téma!="matematika":
		continue
	if pontszám==1:
		pont1+=1
	elif pontszám==2:
		pont2+=1
	else:
		pont3+=1		

print("Az adatfájlban {} matematika feladat van, 1 pontot ér {} feladat, 2 pontot ér {} feladat, 3 pontot ér {} feladat.".format(pont1+pont2+pont3,pont1,pont2,pont3) )

#--- 4. feladat ---
print("\n4. feladat:")

def hasonlítandó( feladat):
	#kérdés,válaszérték,pont,téma= feladat
	#return válaszérték
	return feladat[1]

# Példaképpen kétféle módon adjuk meg a 'key'-t:
legkisebb= min(adatok,key= hasonlítandó)
legnagyobb= max(adatok,key= lambda feladat: feladat[1])

print("A válaszok számértékének intervalluma: {}-{}".format( legkisebb[1],legnagyobb[1] ))

#--- 5. feladat ---
print("\n5. feladat:")
témák=set()
for kérdés,válaszérték,pont,téma in adatok:
	témák.add(téma)
print("A témakörök:", ",".join(témák))

#--- 6. feladat ---
print("\n6. feladat:")
import random
random.seed()

kért_téma= input("Milyen témakörből szeretne kérdést kapni? ").strip()

válogatás= [ (kérdés,válaszérték,pont,téma) for (kérdés,válaszérték,pont,téma) in adatok if téma==kért_téma ]
#válogatás= [ feladat for feladat in adatok if feladat[-1]==kért_téma ]

kérdés,válaszérték,pont,téma= random.choice(válogatás)

megadott_válasz= int(input(kérdés+" ").strip())
szerzett_pont= pont if megadott_válasz==válaszérték else 0

print("A válasz",szerzett_pont, "pontot ér.")
if not szerzett_pont:
	print("A helyes válasz:", válaszérték)

#--- 7. feladat ---
#print("\n7. feladat:")
feladatsor= random.sample( adatok,10) 

with open("tesztfel.txt","w") as ff:
	összpontszám=0
	for feladat in feladatsor:
		kérdés,válaszérték,pont,téma= feladat
		ff.write( "{} {} {}\n".format(pont,válaszérték,kérdés) )
		összpontszám+= pont
	ff.write("A feladatsorra összesen {} pont adható.".format(összpontszám))

#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben


