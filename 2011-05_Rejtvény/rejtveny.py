#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# rejtveny.py
# Érettségi feladat: 2011. május, Rejtvény
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2016

#--- 1. feladat ---
print("\n1. feladat:")

vsor,voszlop,hajók= input("Adja meg a torony adatait (sor oszlop hajók):").split()
vsor,voszlop,hajók= int(vsor),int(voszlop),int(hajók)
if hajók>3:
	print("Nehéz torony.")

#--- 2. feladat ---
print("\n2. feladat:")

delta=( (-1,-1),(-1,0),(-1,1), (0,1),(1,1), (1,0),(1,-1), (0,-1) ) 
for dsor,doszlop in delta: # a szomszéd koordináták számítása
	ps,po= vsor+dsor,voszlop+doszlop
	if 1<= ps <=10  and  1<= po <=10:	# ha benne van a tartományban, akkor itt nem lehet hajó
		print("{},{}".format(ps,po))	# ps,po "logikai" indexek 1-10-ig, és nem 0-9-ig.
		
#--- 3. feladat ---
print("\n3. feladat:")

rejtvény=[]
with open("feladvany.txt") as ff:
	for sor in ff:
		sor= [ int(p) for p in sor.split() ]
		rejtvény.append(sor)

megoldások=[]
with open("megoldas.txt") as ff:
	darab= int(next(ff))
	for eset in range(darab):
		
		név=next(ff).strip()	# levágjuk a "\n"-t (és a whitespace-ket is)
		megoldás=[]
		for sor in range(10):
			sor= next(ff)
			sor= [ int(p) for p in sor.split() ]
			megoldás.append(sor)
			
		megoldások.append( (név,megoldás) )	
				

def torony( érték):
	return 1<=érték<=9

tévesztők=[]
for név,megoldás in megoldások:

	tévesztett=None
	for s in range(10):
		for o in range(10):
			if torony( rejtvény[s][o]):
				if not torony( megoldás[s][o] ):
					tévesztett= név
					#print(név,s+1,o+1)
					break
			else:
				if torony( megoldás[s][o] ):
					tévesztett= név
					#print(név,s+1,o+1)
					break
		if tévesztett:
			tévesztők.append(név)
			break
			
if tévesztők:
		for név in tévesztők:
			print(név)
else:
	print("Mindegyik megoldás erre a heti feladványra érkezett.")

#--- 4. feladat ---
print("\n4. feladat:")

HAJÓ=11
hajóhiba=[]
for név,megoldás in megoldások:

	if név in tévesztők:
		continue	# Csak az aktuális heti feladvány megoldásaival kell foglalkozni.
	hajók=0
	for sor in megoldás:
		hajók+= sor.count(HAJÓ)
		
	if hajók!=12:
		hajóhiba.append(név)

print("A hibás megoldások száma:",len(hajóhiba))
#print(hajóhiba)

#--- 5. feladat ---
print("\n5. feladat:")

VÍZ=0
szabálytalan=[]
for név,megoldás in megoldások:

	hibás=False
	if név in tévesztők or név in hajóhiba:
		continue

	for s in range(10):
		for o in range(10):
			if megoldás[s][o]!= HAJÓ:
				continue
			for dsor,doszlop in delta:
				ps,po= s+dsor,o+doszlop		# ps,po most 0-tól induló indexek!
				if 0<= ps <=9  and  0<= po <=9  and  megoldás[ps][po]!=VÍZ:
					hibás=True
					#print(név,ps+1,po+1)
					break
			if hibás:
				break

		if hibás:
			break

	if hibás:
		szabálytalan.append(név)

print("A szabálytalan megoldások száma:",len(szabálytalan))
#print(szabálytalan)


#--- 6. feladat ---
print("\n6. feladat:")

helyesek=[]
for név,megoldás in megoldások:

	helyes=True
	
	if név in tévesztők or név in hajóhiba or név in szabálytalan:
		continue

	for s in range(10):
		for o in range(10):
			érték= megoldás[s][o]
			if not torony(érték):
				continue
			látott_hajók= megoldás[s].count(HAJÓ)
			látott_hajók+= len( [ 1 for i in range(10) if megoldás[i][o]==HAJÓ] )
			if látott_hajók != érték:
				helyes=False
				break
		if not helyes:
			break

	else:
		helyesek.append(név)

print("A helyes megoldások száma:",len(helyesek))
print(", ".join(helyesek))						

#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben



