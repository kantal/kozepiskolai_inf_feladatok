#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# ut.py
# Érettségi feladat: 2009. október, Útépítés
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2016

#--- 1. feladat ---
print("\n1. feladat")
járművek=[]
with open("forgalom.txt") as ff:
	tételszám= int(next(ff))	# Az első sor feldolgozása.
	for sor in ff:
		óra,perc,mp,tartam,honnan= sor.split()
		járművek.append( [int(óra),int(perc),int(mp),int(tartam),honnan] )

#--- 2. feladat ---
print("\n2. feladat")
sorszám= int(input("Adja meg a jármű sorszámát(1-{}): ".format(tételszám)))
print("A(z) {}. jármű {} város felé haladt.".format( sorszám, "Alsó" if járművek[sorszám-1][4]=="F" else "Felső"))

#--- 3. feladat ---
print("\n3. feladat")
utolsók=[]
for i in range(len(járművek)-1,-1,-1):	# visszafelé keresünk
	if len(utolsók)==2:
		break
	óra,perc,mp,tartam,honnan= járművek[i]
	if honnan=="A":
		utolsók.append(járművek[i])

ó1,p1,mp1,t1,i1= utolsók[1] # korábbi
ó2,p2,mp2,t2,i2= utolsók[0] # későbbi

print("A Felső város felé tartó két utolsó jármű a szakasz elejére",(ó2-ó1)*3600+(p2-p1)*60+mp2-mp1,"mp különbséggel érkezett.")

#--- 4. feladat ---
print("\n4. feladat")
statisztika= [ [0 for i in range(2)] for óra in range(24) ] # [ [alsóból,felsőből], ... ]
for óra,perc,mp,tartam,honnan in járművek:
	if honnan=="A":
		statisztika[óra][0]+= 1
	else:
		statisztika[óra][1]+= 1

for óra,adat in enumerate(statisztika):
	if adat!=[0,0]:
		print(óra,adat[0],adat[1])		

#--- 5. feladat ---
print("\n5. feladat")
# A sorba rendezést az adatok egy másolatán végezzük el, mert az eredeti sorrendre
# még szükség lesz a következő feladatban.
# A másolat létrehozására többféle módszer közül választhatunk:
#
# 1. Az 1. feladat kódját függvénnyé alakítjuk és meghívjuk.
#
# 2. A 'járművek' objektumból *teljes körű* másolással készítünk egy új objektumot:
#		import copy
#		járművek2= copy.deepcopy(járművek)
#
# 3. A 'járművek' objektumból *alapszintű másolással* készítünk egy új objektumot, például:
#		import copy
#		járművek2= copy.copy(járművek)
#
#		amit egy listánál egyszerűbben így is megtehetünk:		járművek2= list(járművek)
#		de még így is:											járművek2= járművek[:]
#		vagy a Python 3.3 verziójától kezdve:					járművek2= járművek.copy()
#
# Ha egy bonyulaltabb adatszerkezetnél nem tudjuk a vizsga izgalmában eldönteni, hogy
# elegendő-e az alapszintű másolat vagy teljes körűt kell készíteni, akkor válasszuk az utóbbit.

# ---
# A sebesség szerint csökkenő sorrendben kell rendezni. A nagyobb sebesség kisebb áthaladási időnek,
# azaz kisebb 'tartamnak' felel meg. Egy rendezés, ha nem adjuk meg a "reverse=True" utasítást, akkor
# növekvő sorrendet eredményez. Így a 'tartam' szerinti növekvő rendezés megfelelő lesz.
def hasonlítandó( tétel):	# A "beszédes" változat.
	óra,perc,mp,tartam,honnan= tétel
	return tartam

#def hasonlítandó( tétel):	# A rövid változat.
#	return tétel[3]
	
# Most az alapszintű másolat is megfelel:
járművek2=list(járművek)
járművek2.sort(key=hasonlítandó)	

# Az alapszintű másolást és a sorba rendezést egyszerre is elvégezhettük volna a sorted() standard függvénnyel:
#járművek2= sorted(járművek,key=hasonlítandó)
# Sőt lambda függvényt is használhatunk, s ekkor nincs szükség a hasonlítandó() fgv.-re:
#járművek2= sorted(járművek,key=lambda tétel: tétel[3])

for i in range(0,10):
	óra,perc,mp,tartam,honnan= járművek2[i]
	print(óra,perc,mp,honnan, round(1000/tartam,1) )

#--- 6. feladat ---
print("\n6. feladat")
def másodperc( óra,perc,mp):
	return óra*3600+perc*60+mp

def időpont( mperc):
	óra= mperc//3600
	perc= (mperc-3600*óra)//60
	mp= mperc%60
	return óra,perc,mp

with open("also.txt","w") as ff:
	
	előző_érkezés_mp=0
	óra,perc,mp=0,0,0
		
	for (ióra,iperc,imp,tartam,honnan) in járművek:
		
		if honnan=="F":
			érkezés_mp= másodperc(ióra,iperc,imp)+tartam
			if érkezés_mp > előző_érkezés_mp:
				óra,perc,mp= időpont(érkezés_mp)
				előző_érkezés_mp= érkezés_mp

			ff.write("{} {} {}\n".format(óra,perc,mp))
		
#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben


