#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# radio.py
# Érettségi feladat, 2015. május, Expedíció
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2016

#--- 1. feladat ---
#print("\n1. feladat")
adatok=[]
with open("veetel.txt") as ff:
	for sor in ff:
		nap,rádiós = sor.split()	
		távirat= next(ff).strip()	
		adatok.append( (int(nap),int(rádiós),távirat) )
#print(adatok)	# szemrevételezés

#--- 2. feladat ---
print("\n2. feladat")
print("Az első üzenet rögzítője:",adatok[0][1])
print("Az utolsó üzenet rögzítője:",adatok[-1][1])

#--- 3. feladat ---
print("\n3. feladat")
for nap,rádiós,távirat in adatok:
	if "farkas" in távirat:
		print("{}. nap {}. rádióamatőr".format(nap,rádiós))
		
#--- 4. feladat ---
print("\n4. feladat")
naponta= [0]*11		# 11 nap
for nap,rádiós,távirat in adatok:
	naponta[nap-1]+= 1
		
for index,rádiósok in enumerate(naponta):
	print("{}. nap: {} rádióamatőr".format(index+1,rádiósok))
	
#--- 5. feladat ---
#print("\n5. feladat")
# Egy egyszerű (de nem igazán optimális) megoldás
with open("adaas.txt","w") as ff:

	for napsorszám in range(1,12):		# 1-11
	
		napi_vétel= [ távirat for nap,rádiós,távirat in adatok if nap==napsorszám ]
		korrigált= ['#']*90
		for távirat in napi_vétel:
			for index,karakter in enumerate(távirat):
				if karakter!='#':
					korrigált[index]= karakter
				
		ff.write( "".join(korrigált)+"\n" )

#--- 6. feladat ---
#print("\n6. feladat")
# Az alábbi algoritmus nem igazán jó. Egyrészt egy üres karakterlánc 
# esetén is igazat ad vissza, másrészt a ciklusból érdemes lenne
# kiugrania, ha olyan karaktert talált, ami nem számjegy.
		
#Függvény szame(szo:karaktersorozat): logikai
#	valasz:=igaz
#	Ciklus i:=1-től hossz(szo)-ig
#		ha szo[i]<'0' vagy szo[i]>'9' akkor valasz:=hamis
#	Ciklus vége
#	szame:=valasz
#Függvény vége

# A szolgai megoldás, ami helyett egyébként az isdigit() metódust
# fogjuk használni:
def szame( szo):
	valasz= True
	for i in range(len(szo)):
		if szo[i]<'0' or szo[i]>'9':
			valasz=False
			#break
	return valasz

#--- 7. feladat ---
print("\n7. feladat")	
megadott_nap= int( input("Adja meg a nap sorszámát! "))
megadott_rádiós= int( input("Adja meg a rádióamatőr sorszámát! "))

feljegyzés=""
for nap,rádiós,távirat in adatok:
	if nap==megadott_nap and rádiós==megadott_rádiós:
		feljegyzés= távirat
		break

if not feljegyzés:
	print("Nincs ilyen feljegyzés")
else:
	egyedek= feljegyzés.split(" ",1)[0].split("/",1)
	if len(egyedek)==2 and egyedek[0].isdigit() and egyedek[1].isdigit():
			print("A megfigyelt egyedek száma:", int(egyedek[0])+int(egyedek[1]) )
	else:
		print("Nincs információ")

#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben


	
