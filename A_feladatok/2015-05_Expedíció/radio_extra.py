#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# extra_radio.py
# A 2015. májusi érettségi feladat alapján, Expedíció
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2016

#--- 1. feladat ---
#print("\n1. feladat")
adatok=[]
with open("veetel.txt") as ff:
	for sor in ff:
		sor=sor.split()
		if not sor:
			continue
			
		if len(sor)!=2 or not sor[0].isdigit() or not sor[1].isdigit():
			print("Hibás adatok")
			exit(1)

		try:			
			távirat= next(ff).strip()
			while not távirat:
				távirat= next(ff).strip()
		except StopIteration:
			print("Nem megfelelő számú sor")
			exit(1)
			
		adatok.append( (int(sor[0]),int(sor[1]),távirat) ) # (nap,rádiós,távirat)

if not adatok:
	print("Nincs feldolgozható adat")
	exit(1)

nap,rádiós,távirat= adatok[0]
távirathossz= len(távirat)		# len(adatok[0][2])
for nap,rádiós,távirat in adatok:
	if távirathossz !=	len(távirat):
		print("Nem egyező távirathosszak")
		exit(1)

#--- 2. feladat ---
print("\n2. feladat")
print("Az első üzenet rögzítője:",adatok[0][1])
print("Az utolsó üzenet rögzítője:",adatok[-1][1])

#--- 3. feladat ---
print("\n3. feladat")
for nap,rádiós,távirat in adatok:
	if "farkas" in távirat.lower():
		print("{}. nap {}. rádióamatőr".format(nap,rádiós))
		
#--- 4. feladat ---
print("\n4. feladat")
naponta=dict()
for nap,rádiós,távirat in adatok:
	naponta[nap]= naponta.get(nap,0)+1

utolsó_nap= max( naponta.keys() )

for nap in range(1,utolsó_nap+1):
	print("{}. nap: {} rádióamatőr".format( nap,naponta.get(nap,0) ))
	
#--- 5. feladat ---
#print("\n5. feladat")
with open("adaas.txt","w") as ff:

	for napsorszám in range(1,utolsó_nap+1):		
	
		napi_vétel= [ távirat for nap,rádiós,távirat in adatok if nap==napsorszám ]
		korrigált= []
		for karindex in range(távirathossz):
			for távindex in range(len(napi_vétel)):
				kar= napi_vétel[távindex][karindex]
				if kar!="#":
					korrigált.append(kar)
					break
			else:
				korrigált.append("#")
				
		ff.write( "".join(korrigált)+"\n" )

#--- 6. feladat ---
#print("\n6. feladat")
# Az alábbi algoritmus nem igazán jó. Egyrészt egy üres karakterlánc 
# esetén is igazat ad vissza, másrészt a ciklusból érdemes kiugrani, 
# ha olyan karaktert talált, ami nem számjegy.

#Függvény szame(szo:karaktersorozat): logikai
#	valasz:=igaz
#	Ciklus i:=1-től hossz(szo)-ig
#		ha szo[i]<'0' vagy szo[i]>'9' akkor valasz:=hamis
#	Ciklus vége
#	szame:=valasz
#Függvény vége

# Egy jobb és pythonosabb megoldás (de nem fogjuk használni):
def szame(szo):
	if not szo:
		return False
	for k in szo:
		if k<'0' or k>'9':
			return False
	return True

#--- 7. feladat ---
print("\n7. feladat")	

try:
	megadott_nap= int( input("Adja meg a nap sorszámát! "))
	megadott_rádiós= int( input("Adja meg a rádióamatőr sorszámát! "))
except ValueError:
	print("Hibás számmegadás!")
	exit(1)	

feljegyzés=""
for nap,rádiós,távirat in adatok:
	if nap==megadott_nap and rádiós==megadott_rádiós:
		feljegyzés= távirat
		break

if not feljegyzés:
	print("Nincs ilyen feljegyzés")
else:
	try:
		kifejlett,kölyök= feljegyzés.split(" ",1)[0].split("/",1)
		print("A megfigyelt egyedek száma:", int(kifejlett)+int(kölyök) )
	except ValueError:
		print("Nincs információ")
	
#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben

