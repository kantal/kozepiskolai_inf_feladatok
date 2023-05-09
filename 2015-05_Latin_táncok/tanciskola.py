#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# tanciskola.py
# Érettségi feladat: 2015. május, Latin táncok
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2016

#--- 1. feladat ---
#print("\n1. feladat")
táncrend=[]
with open("tancrend.txt") as ff:
	for sor in ff:
		tánc= sor.strip()
		lány= next(ff).strip()
		fiú=  next(ff).strip()
		táncrend.append( (tánc,lány,fiú) )
#print(táncrend)	# szemrevételezés

#--- 2. feladat ---
print("\n2. feladat")
print("Az elsőként bemutatott tánc:", táncrend[0][0])
print("Az utolsóként bemutatott tánc:", táncrend[-1][0])

#--- 3. feladat ---
print("\n3. feladat")
samba=0
for (tánc,lány,fiú) in táncrend:
	if tánc=="samba":
		samba+= 1
print("A sambát", samba, "pár mutatta be")

#--- 4. feladat---
print("\n4. feladat")
print("Vilma ezekben a táncokban szerepelt:")
for (tánc,lány,fiú) in táncrend:
	if lány=="Vilma":
		print(tánc)

#--- 5. feladat ---
print("\n5. feladat")
megadott_tánc= input("Adjon meg egy táncot: ").strip()
táncolt=False
for (tánc,lány,fiú) in táncrend:
	if lány=="Vilma" and tánc==megadott_tánc:
		táncolt=True
		print("A",megadott_tánc,"bemutatóján Vilma párja", fiú,"volt.")
		break
		
if not táncolt:
	print("Vilma nem táncolt",megadott_tánc+"-t")
	
#--- 6. feladat ---
#print("\n6. feladat")
lányok=set()
fiúk=set()

for (tánc,lány,fiú) in táncrend:
	lányok.add(lány)
	fiúk.add(fiú)
#print(lányok,fiúk)	# szemrevételezés

with open("szereplok.txt","w") as ff:
	
	ff.write("Lányok: "+ ", ".join(lányok) +"\n")	
	ff.write("Fiúk: "+ ", ".join(fiúk) +"\n")
	
#--- 7. feladat ---
print("\n7. feladat")
lányok=dict()
fiúk=dict()

for (tánc,lány,fiú) in táncrend:
	lányok[lány]= lányok.get(lány,0)+1
	fiúk[fiú]= fiúk.get(fiú,0)+1
#print(lányok,fiúk)	# szemrevételezés
	
#--- Fiúk
legtöbb= max( fiúk.values() )
szorgalmasak=[ táncos for (táncos,eset) in fiúk.items() if eset==legtöbb ]
print("A legtöbbet szereplő fiú(k): "+ ", ".join(szorgalmasak) )

#--- Lányok
legtöbb= max( lányok.values() )
szorgalmasak=[ táncos for (táncos,eset) in lányok.items() if eset==legtöbb ]
print("A legtöbbet szereplő lány(ok): "+ ", ".join(szorgalmasak) )


#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben


