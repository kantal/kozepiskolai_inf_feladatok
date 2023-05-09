#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# szavak.py
# Érettségi feladat: 2011. május, Szójáték
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2016

#--- 1. feladat ---
print("\n1. feladat:")

szó= input("Adjon meg egy szót: ").strip().lower()
magánhangzók= "aáeéiíoóöőuúüű"

for betű in magánhangzók:
	if betű in szó:
		print("Van benne magánhangzó.")
		break
else:
	print("Nincs benne magánhangzó.")
		
#--- 2. feladat ---
print("\n2. feladat:")

leghosszabb=None
hossz=0
with open("szoveg.txt") as ff:
	for szó in ff:
		szó=szó.strip()
		if len(szó) > hossz:
			leghosszabb,hossz= szó,len(szó)

print("A leghosszabb szó ({}): {}".format(hossz,leghosszabb))

#--- 3. feladat ---
print("\n3. feladat:")

összes=0
magánhangzós=0
with open("szoveg.txt") as ff:
	for szó in ff:
		szó=szó.strip()
		összes+=1
		magánszám= len( [betű for betű in szó if betű in magánhangzók] )
		if len(szó) < 2*magánszám:
			magánhangzós+=1
			print(szó,end=" ")

print("\n{}/{} : {:.2f}%".format(magánhangzós,összes, magánhangzós*100/összes ))

#--- 4. feladat ---
print("\n4. feladat:")
ötösök=[]	
with open("szoveg.txt") as ff:
	for szó in ff:
		szó=szó.strip()
		if len(szó)==5:
			ötösök.append(szó)

szórészlet= input("Adjon meg egy 3 karakteres szórészletet: ").strip().lower()
if len(szórészlet)!=3:
	print("Hibás hossz!")

szólétra=[ szó for szó in ötösök if szó[1:4]==szórészlet ]
print(" ".join(szólétra))

#--- 5. feladat ---
#print("\n5. feladat:")

with open("letra.txt","w") as ff:
	
	while ötösök:
		részlet= ötösök[0][1:4]
		létra= [ szó for szó in ötösök if részlet==szó[1:4] ]
		if len(létra)>1:
			ff.write("\n".join(létra)+"\n\n")
		for szó in létra:
			ötösök.remove(szó)

#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben


