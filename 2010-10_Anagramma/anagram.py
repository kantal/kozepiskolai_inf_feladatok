#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# anagram.py
# Érettségi feladat: 2010. október, Anagramma
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2016

#--- 1. feladat ---
print("\n1. feladat:")
szöveg= input("Adjon meg egy szöveget: ").lower()
dd=dict()
for kar in szöveg:
	dd[kar]= dd.get(kar,0)+1

print("A különböző karakterek száma:",len(dd))
for kar in dd:
	print( kar+": ",dd[kar])	

# Rendezett kiírás:
#ll= list(dd.items())
#ll.sort( key=lambda kar_db: kar_db[1], reverse=True)
#for (kar,db) in ll:
#	print( kar+": ",db)

#--- 2. feladat ---
#print("\n2. feladat:")

szavak=[]
with open("szotar.txt") as ff:
	for sor in ff:
		sor=sor.strip()
		if sor:
			szavak.append(sor)

#--- 3. feladat ---
#print("\n3. feladat:")

with open("abc.txt","w") as ff:
	for szó in szavak:
		ff.write( "".join(sorted(szó))+"\n" )

#--- 4. feladat ---
print("\n4. feladat:")

szó1= input("Adja meg az első szót: ").strip().lower()
szó2= input("Adja meg a második szót: ").strip().lower()

if sorted(szó1)==sorted(szó2):
	print("Anagramma")
else:
	print("Nem anagramma")
	
#--- 5. feladat ---
print("\n5. feladat:")

adott_szó= input("Adjon meg egy szót: ").strip().lower()
rendezett= sorted(adott_szó)
anagrammák= [ szó for szó in szavak if sorted(szó)==rendezett ]
if anagrammák:
	for szó in anagrammák:
		print(szó)
else:
	print("Nincs a szótárban anagramma")

#--- 6. feladat ---
print("\n6. feladat:")

leghosszabb_szó= max( szavak, key=len)
max_hossz= len(leghosszabb_szó)

leghosszabbak= [ szó for szó in szavak if len(szó)==max_hossz ]
# Rendezni fogjuk a leghosszabb szavakat úgy, hogy az egy anagrammának megfelelőek egymás mellé kerüljenek.
# Ezért a rendezés kulcsaként, a lexikografikus (betű szerinti) rendezéshez nem a szavak eredeti alakját adjuk
# meg, hanem azt, amelyben a karaktereket sorba rendeztük. Ehhez a sorted() függvényt használjuk fel, ami ugyan
# nem karakterláncot (szót) ad vissza, hanem a szó karaktereit egy listában, de ez nem jelent problémát, ha az
# összehasonlításokban mindig ilyent használunk.

def hasonlítandó(szó):
	return sorted(szó)

leghosszabbak.sort( key=hasonlítandó)
#leghosszabbak.sort( key=sorted)

for szó in leghosszabbak:
		print(szó)

#--- 7. feladat ---
#print("\n7. feladat:")

min_hossz= len( min( szavak, key=len) )

with open("rendezve.txt","w") as ff:

	for hossz in range(min_hossz,max_hossz+1):

		l= [ szó for szó in szavak if len(szó)==hossz ]
		nem_üres= True if l else False
		while l:
			rendezett= sorted(l[0])
			ana= [ szó for szó in l if sorted(szó)==rendezett ]
			ff.write( " ".join(ana)+"\n")
			for szó in ana:
				l.remove(szó)
		
		if nem_üres:
			ff.write("\n")


#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben


