#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# zar.py
# Érettségi feladat, 2016. május, Zár
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2016

#--- 1. feladat ---
#print("\n1. feladat")
with open("ajto.txt") as ff:
	kódsorok=[ kódsor.strip() for kódsor in ff ]

#--- 2. feladat ---
print("\n2. feladat")
megadott_kód= input("Adja meg, mi nyitja a zárat! ").strip()

#--- 3. feladat ---
print("\n3. feladat")
print("A nyitó kódszámok sorai:",end=" ")
for index,kód in enumerate(kódsorok):
	if kód==megadott_kód:
		print( index+1,end=" ")
print()
		
#--- 4. feladat ---
print("\n4. feladat")
for index,kód in enumerate(kódsorok):
	if len(kód) != len(set(kód)):
		print("Az első ismétlődést tartalmazó próbálkozás sorszáma:", index+1)
		break
else:		
	print("Nem volt ismétlődő számjegy")

#--- 5. feladat ---
print("\n5. feladat")
import random
random.seed()

hossz=len(megadott_kód)
véletlen_kód= random.sample("0123456789",hossz)
print("Egy",hossz,"hosszú kódszám:",  "".join(véletlen_kód))

#--- 6. feladat ---
#print("\n6. feladat")
#	Függvény nyit(jo, proba:karaktersorozat): logikai érték
#		egyezik:=(hossz(jo)=hossz(proba))
#		Ha egyezik akkor
#			elteres=ascii(jo[1])-ascii(proba[1])
#			Ciklus i:=2-től hossz(jo)
#				Ha ( elteres - (ascii(jo[i])-ascii(proba[i])) ) mod 10 <> 0
#				akkor egyezik:=hamis
#			Ciklus vége
#		Elágazás vége
#		nyit:=egyezik
#	Függvény vége

def nyit(jo,proba):
	egyezik= len(jo)==len(proba)
	if egyezik:
		elteres=ord(jo[0])-ord(proba[0])
		for i in range(1,len(jo)):
			if (elteres - (ord(jo[i])-ord(proba[i])) ) % 10 != 0:
				egyezik= False
				break
	return egyezik

#print("teszt: ",nyit("017239","239451"))	

#--- 7. feladat ---
#print("\n7. feladat")
with open("siker.txt","w") as ff:
	for kód in kódsorok:
		if( len(kód) != len(megadott_kód)):
			ff.write(kód+" hibás hossz\n")
		else:
			if nyit(kód,megadott_kód):
				ff.write(kód+" sikeres\n")	
			else:
				ff.write(kód+" hibás kódszám\n")

#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben

				
