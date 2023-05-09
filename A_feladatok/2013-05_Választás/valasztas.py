#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# valasztas.py,
# Érettségi feladat: 2013. május, Választások
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2016

#--- 1. feladat ---
#print("\n1. feladat:")
választás=[]
with open("szavazatok.txt") as ff:
	for sor in ff:
		körzet,szavazat,csnév,unév,szervezet= sor.split()
		választás.append( (int(körzet),int(szavazat),csnév,unév,szervezet) )

#--- 2. feladat ---
print("\n2. feladat:")		
print("A helyhatósági választáson",len(választás),"képviselőjelölt indult.")

#--- 3. feladat ---
print("\n3. feladat:")	
megadott_csnév,megadott_unév= input("Adja meg egy képviselő nevét! (vezeték- és utónév) ").split()
for körzet,szavazat,csnév,unév,szervezet in választás:
	if csnév==megadott_csnév and unév==megadott_unév:
		print("A kapott szavazatok száma:",szavazat)
		break
else:
	print("Ilyen nevű képviselőjelölt nem szerepel a nyilvántartásban!")
	
#--- 4. feladat ---
print("\n4. feladat:")
jogosultak=12345
résztvevők=0
for körzet,szavazat,csnév,unév,szervezet in választás:
	résztvevők+=szavazat

print("A választáson {0} állampolgár, a jogosultak {1:.2f}%-a vett részt.".format(résztvevők, résztvevők/jogosultak*100))

#--- 5. feladat ---
print("\n5. feladat:")
eredmények=dict()
for körzet,szavazat,csnév,unév,szervezet in választás:
	eredmények[szervezet]= eredmények.get(szervezet,0)+szavazat

szervezetek={ "GYEP":"Gyümölcsevők Pártja","HEP":"Húsevők Pártja","TISZ":"Tejivók Szövetsége","ZEP":"Zöldségevők Pártja","-":"Független jelöltek"}

for szervezet in eredmények:
	print("{0}= {1:.2f}%".format( szervezetek[szervezet],eredmények[szervezet]/résztvevők*100))

#--- 6. feladat ---
print("\n6. feladat:")

def hasonlítandó( tétel ):
	körzet,szavazat,csnév,unév,szervezet= tétel
	return szavazat

legtöbbet_kapott= max(választás,key=hasonlítandó)
legtöbb= legtöbbet_kapott[1]
#legtöbbet_kapott=[ tétel for tétel in választás if tétel[1]==legtöbb ]
legtöbbet_kapott=[ (körzet,szavazat,csnév,unév,szervezet) for (körzet,szavazat,csnév,unév,szervezet) in választás if szavazat==legtöbb ]

#print("A legtöbb szavazatot ({}) kapt{}:".format(legtöbb, "ák" if len(legtöbbet_kapott)>1 else "a" ))
print("A legtöbb szavazatot ({}) kapta:".format(legtöbb) )
for körzet,szavazat,csnév,unév,szervezet in legtöbbet_kapott:
	print("{} {}, {}".format(csnév,unév, "független" if szervezet=="-" else szervezet))

#--- 7. feladat ---
#print("\n7. feladat:")
with open("kepviselok.txt","w") as ff:
	ff.write("A megválasztott képviselők:\n")
	
	for kerület in range(1,9):
		eredmény=[ (körzet,szavazat,csnév,unév,szervezet) for (körzet,szavazat,csnév,unév,szervezet) in választás if körzet==kerület]
		körzet,szavazat,csnév,unév,szervezet= max(eredmény,key=hasonlítandó) 
		ff.write("{} {} {} {}\n".format(körzet,csnév,unév,"független" if szervezet=="-" else szervezet ) )	
		
#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben


