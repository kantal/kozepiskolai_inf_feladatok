#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# szinkep.py,
# Érettségi feladat: 2012. október, Színkép
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2016

#--- 1. feladat ---
#print("\n1. feladat:")
kép=[]
with open("kep.txt") as ff:
	pontsor=[]
	for index,sor in enumerate(ff):
		if pontsor and index%50==0:
			kép.append(pontsor)
			pontsor=[]
		pontsor.append( sor.split() )

kép.append(pontsor)
				
#--- 2. feladat ---
print("\n2. feladat:")
rgb=input("Adjon meg egy RGB színkódot az értékeket szóközzel elválasztva: ")
rgb= rgb.split()
van=False
for sor in kép:
	for pont in sor:
		if pont==rgb:
			van=True
			break
	if van:
		print("A megadott szín szerepel a képen.")
		break
else:
	print("A megadott szín nem szerepel a képen.")

#--- 3. feladat ---
print("\n3. feladat:")			
s35p8=kép[34][7]
db_sor35=kép[34].count(s35p8)
db_oszlop8=0
for sor in kép:
	if sor[7]==s35p8:
		db_oszlop8+=1

print("Sorban: {} Oszlopban: {}".format(db_sor35,db_oszlop8))


#--- 4. feladat ---
print("\n4. feladat:")
red=["255","0","0"]
green=["0","255","0"]
blue=["0","0","255"]

vörösök,zöldek,kékek=0,0,0
for sor in kép:
	for pont in sor:
		if pont==red:
			vörösök+=1
		elif pont==blue:
			kékek+=1
		elif pont==green:
			zöldek+=1

legtöbb= max( (vörösök,"vörös"),(kékek,"kék"),(zöldek,"zöld") )
#print((vörösök,"vörös"),(kékek,"kék"),(zöldek,"zöld") )	
print("A vörös, kék és zöld közül az egyik legtöbbször előforduló szín a {}.".format(legtöbb[1]) )

#--- 5. feladat ---
#print("\n5. feladat:")
fekete=["0","0","0"]
for s in range(3):
	for o in range(50):
		kép[s][o]= fekete
		kép[49-s][o]= fekete

for o in range(3):
	for s in range(3,47):
		kép[s][o]= fekete
		kép[s][49-o]= fekete

#--- 6. feladat ---
#print("\n6. feladat:")		
with open("keretes.txt","w") as ff:
	for sor in kép:
		for pont in sor:
			ff.write(" ".join(pont)+"\n")

#--- 7. feladat ---
print("\n7. feladat:")	
sárga=["255","255","0"]			
# Feltételezzük, hogy csak a keresendő téglalapban van sárga szín.
bal_felső=None
for sor in range(50):
	for oszlop in range(50):
		if kép[sor][oszlop]==sárga:
			bal_felső=(sor,oszlop)
			break
	if bal_felső:
		break
print("Kezd: {},{}".format( bal_felső[0]+1,bal_felső[1]+1))

jobb_alsó=None
for sor in range(49,-1,-1):
	for oszlop in range(49,-1,-1):
		if kép[sor][oszlop]==sárga:
			jobb_alsó=(sor,oszlop)
			break
	if jobb_alsó:
		break
print("Vége: {},{}".format( jobb_alsó[0]+1,jobb_alsó[1]+1))

print("Képpontok száma:",(jobb_alsó[0]-bal_felső[0]+1)*(jobb_alsó[1]-bal_felső[1]+1) )


#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben


