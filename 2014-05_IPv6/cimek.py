#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# cimek.py,
# Érettségi feladat: 2014. május, IPv6
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2016

#--- 1. feladat ---
#print("\n1. feladat:")
címek=[]
with open("ip.txt") as ff:
	for sor in ff:
		sor=sor.strip()
		if sor:
			címek.append(sor)

#--- 2. feladat ---
print("\n2. feladat:")	
print("Az állományban",len(címek),"darab adatsor van.")

#--- 3. feladat ---
print("\n3. feladat:")
print("A legalacsonyabb tárolt IP-cím:\n", min(címek))

#--- 4. feladat ---
print("\n4. feladat:")
print("Dokumentációs cím:", len( [ cím for cím in címek if cím.startswith("2001:0db8")] ) )
print("Globális egyedi cím:", len( [ cím for cím in címek if cím.startswith("2001:0e")] ) )
print("Helyi egyedi cím:", len( [ cím for cím in címek if cím.startswith("fc") or cím.startswith("fd")] ) )

#--- 5. feladat ---
#print("\n5. feladat:")
with open("sok.txt","w") as ff:
	for index,cím in enumerate(címek):
		if cím.count('0')>=18:
			ff.write("{} {}\n".format(index+1,cím))
			
#--- 6. feladat ---
print("\n6. feladat:")
sorszám= int(input("Kérek egy sorszámot: "))
if sorszám<1 or sorszám>len(címek):
	print("Hibás sorszám!")
	
cím= címek[sorszám-1]
tagok= cím.split(":")
for i in range(len(tagok)):
	tag= tagok[i].lstrip("0")
	tagok[i]= "0" if not tag else tag

print(cím+"\n"+ ":".join(tagok) )

#--- 7. feladat ---
print("\n7. feladat:")
leghosszabb=0
start_index=None
hossz=0
for index,tag in enumerate(tagok):
	
	if tag=="0":
		hossz+=1
	else:
		if hossz>leghosszabb:
			leghosszabb= hossz
			start_index= index-hossz
			hossz=0

if hossz>leghosszabb:
			leghosszabb= hossz
			start_index= index-hossz			

if leghosszabb>1:	# Csak a kettő vagy több 0-ból álló csoport érdekes számunkra. 0:0
	újcím= ":".join( tagok[:start_index]) + "::" + ":".join( tagok[start_index+leghosszabb:] )
	print( újcím)
else:
	print("Nem rövidíthető tovább.")


#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben


