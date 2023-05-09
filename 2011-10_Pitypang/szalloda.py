#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# szalloda.py
# Érettségi feladat: 2011. október, Pitypang
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2016

#--- 1. feladat ---
#print("\n1. feladat:")
szálloda=[]
with open("pitypang.txt") as ff:
	next(ff)	# tételszám= next(ff)	A tételek számát nem tároljuk el, a len(szalloda) ezzel lesz egyenlő.
	for sor in ff:
		sorszám,szoba,érkezés,távozás,vendégek,reggeli,azonosító= sor.split()
		szálloda.append( [int(szoba),int(érkezés),int(távozás),int(vendégek),int(reggeli),azonosító] )


#--- 2. feladat ---
print("\n2. feladat:")

# A1) Jól olvasható kóddal:
def hasonlítandó(tétel):
	szoba,érkezés,távozás,vendégek,reggeli,azonosító= tétel
	return távozás-érkezés

szoba,érkezés,távozás,vendégek,reggeli,azonosító= max( szálloda,key=hasonlítandó)
print("{} ({}) - {}".format(azonosító,érkezés,távozás-érkezés))

# A2) Indexeléssel:
#def hasonlítandó(tétel):
#	return tétel[2]-tétel[1]
#
#leghosszabb= max( szálloda,key=hasonlítandó)
#print("{} ({}) - {}".format( leghosszabb[-1], leghosszabb[1],leghosszabb[2]-leghosszabb[1]) )

# A3) Lambda-függvénnyel:
#leghosszabb= max( szálloda,key=lambda tétel: tétel[2]-tétel[1])
#print("{} ({}) - {}".format( leghosszabb[-1], leghosszabb[1],leghosszabb[2]-leghosszabb[1]) )

#--- 3. feladat ---
print("\n3. feladat:")

def napidíj(érkezés):
	if érkezés<121:
		return 9000
	if érkezés<244:
		return 10000
	return 8000

with open("bevetel.txt","w") as ff:

	totál=0
	for sorszám,tétel in enumerate(szálloda):
		szoba,érkezés,távozás,vendégek,reggeli,azonosító= tétel
		éjszakák= távozás-érkezés
		pótágy= vendégek-2 if vendégek>2 else 0
		fizetendő= éjszakák*( napidíj(érkezés) + reggeli*vendégek*1100 + pótágy*2000 )
		
		ff.write("{}:{}\n".format(sorszám+1,fizetendő))

		totál+=fizetendő

#print("Az éves bevétel:",totál,"Ft")
print("Az éves bevétel: {0:,} Ft".format(totál))

#--- 4. feladat ---
print("\n4. feladat:")

hónapok=[]
with open("honapok.txt") as ff:
	for sor in ff:
		# hónap_neve= sor	# a hónap nevére nincs szükségünk
		napok= int(next(ff))
		kezdőnap= int(next(ff))
		hónapok.append( (napok,kezdőnap) )	 # hónapok.append( (int(next(ff)),int(next(ff))) )


def hónap_indexe(nap):
	for index,(napok,kezdőnap) in enumerate(hónapok):
		if kezdőnap <= nap < (kezdőnap+napok):		#if kezdőnap<=nap and nap<(kezdőnap+napok):
			return index
	print("Hibás napszám.")


statisztika=[0]*12
for tétel in szálloda:
	szoba,érkezés,távozás,vendégek,reggeli,azonosító= tétel
	for nap in range(érkezés,távozás):
		statisztika[ hónap_indexe(nap) ]+= vendégek

for index,adat in enumerate(statisztika):
	print("{}: {} vendégéj".format(index+1,adat))		


#--- 5. feladat ---
print("\n5. feladat:")
foglalás_eleje= int(input("Adja meg a foglalás kezdő napjának sorszámát: "))
éjszakák_száma= int(input("Adja meg az éjszakák számát: "))

szobák=	[1]*27	# 1/0: szabad/foglalt, True/False
for nap in range(foglalás_eleje,foglalás_eleje+éjszakák_száma):
	for szoba,érkezés,távozás,vendégek,reggeli,azonosító in szálloda:
		if érkezés <= nap < távozás:
			szobák[szoba-1]= 0 	# nem szabad	

szabadok= [ str(index+1) for index,szabad in enumerate(szobák) if szabad ]

if not szabadok:
	print("A megadott időszakban nincs szabad szoba.")
else:
	print("A szabad szobák száma:",len(szabadok))
	print("A szobaszámok:", ",".join(szabadok))

#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben


