#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# otszaz.py
# Érettségi feladat, 2016. május, Ötszáz
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2016

#--- 1. feladat ---
#print("\n1. feladat")
with open("penztar.txt") as ff:

	kosarak=[]
	kosár=[]
	for áru in ff:
		áru= áru.strip()
		if áru=="F":
			kosarak.append(kosár)
			kosár=[]
		else:
			kosár.append(áru)	

#print(kosarak)	# szemrevételezés

#--- 2. feladat ---
print("\n2. feladat")
print("A fizetések száma:", len(kosarak))

#--- 3. feladat ---
print("\n3. feladat")
print("Az első vásárló", len(kosarak[0]), "darab árucikket vásárolt.")

#--- 4. feladat ---
print("\n4. feladat")
sorszám= int(input("Adja meg egy vásárlás sorszámát! "))
árucikk= input("Adja meg egy árucikk nevét! ").strip()
darab= int(input("Adja meg a vásárolt darabszámot! "))

#--- 5. feladat ---
print("\n5. feladat")
kosárválogatás= [ (index,kosár) for (index,kosár) in enumerate(kosarak) if árucikk in kosár ]
print("Az első vásárlás sorszáma:", kosárválogatás[0][0]+1)
print("Az utolsó vásárlás sorszáma:", kosárválogatás[-1][0]+1)
print( len(kosárválogatás),"vásárlás során vettek belőle.")

#--- 6. feladat ---
print("\n6. feladat")

def ertek( db):
	if db==1:
		return 500
	elif db==2:
		return 950
	return 950+(db-2)*400

print( darab, "darab vételekor fizetendő:", ertek(darab) )

#--- 7. feladat ---
print("\n7. feladat")
termékek=dict()
for kacat in kosarak[sorszám-1]:
	termékek[kacat]= termékek.get(kacat,0)+1
	
for kacat in termékek:
	print( termékek[kacat],kacat)	

#--- 8. feladat ---
#print("\n8. feladat")
with open("osszeg.txt","w") as ff:

	for index,kosár in enumerate(kosarak):
		termékek=dict()
		for kacat in kosár:
			termékek[kacat]= termékek.get(kacat,0)+1

		összeg=0;
		for kacat in termékek:
			összeg+= ertek( termékek[kacat])

		ff.write( str(index+1)+": "+str(összeg)+"\n")
		
#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben


