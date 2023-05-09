#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# tort.py
# Érettségi feladat: 2012. május, Törtek
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2016

#--- 1. feladat ---
print("\n1. feladat:")
számláló,nevező= input("Adjon meg egy közönséges törtet (a/b): ").split('/')
számláló,nevező = int(számláló),int(nevező)
maradék= számláló % nevező

if maradék:
	print("Nem egész.")
else:
	print("A tört értéke:", számláló//nevező)

#--- 2. feladat ---
#print("\n2. feladat:")

def lnko(a,b):	# a legnagyobb közös osztó
	if a==b:
		return a
	if a<b:
		return lnko(a,b-a)
	return lnko(a-b,b)	

#--- 3. feladat ---
print("\n3. feladat:")

if not maradék:
	print("{}/{} = {}".format(számláló,nevező, számláló//nevező))
else:
	legnko= lnko(számláló,nevező)
	print("{}/{} = {}/{}".format(számláló,nevező,  számláló//legnko,nevező//legnko))

#--- 4. feladat ---
print("\n4. feladat:")
sz2,n2= input("Adjon meg egy újabb közönséges törtet (a/b): ").split('/')
sz2,n2= int(sz2),int(n2)

eredm_sz= számláló*sz2
eredm_n= nevező*n2
maradék= eredm_sz % eredm_n
legnko= lnko(eredm_sz,eredm_n)

def ts(a,b):	# A törteket megjelenítő kód olvashatóbbá tételére.
	return str(a)+"/"+str(b)
	
#print( "{}/{} * {}/{} = {}/{} = ".format(számláló,nevező,  sz2,n2,  eredm_sz,eredm_n),end="")
print( ts(számláló,nevező),"*",ts(sz2,n2),"=",ts(eredm_sz,eredm_n),"=", end=" ")

if maradék:
	print(ts(eredm_sz//legnko, eredm_n//legnko) )
else:	
	print(eredm_sz//eredm_n)	

#--- 5. feladat ---
#print("\n5. feladat:")

def lkkt(a,b):		# a legkisebb közös töbszörös
	return (a*b)//lnko(a,b)

#--- 6. feladat ---
print("\n6. feladat:")
köznev= lkkt(nevező,n2)
tag1_sz= számláló*köznev//nevező
tag2_sz= sz2*köznev//n2
eredm_sz= tag1_sz + tag2_sz
maradék= eredm_sz % köznev
legnko= lnko(eredm_sz,köznev)

print( ts(számláló,nevező),"+",ts(sz2,n2),"=",ts(tag1_sz,köznev),"+",ts(tag2_sz,köznev),"=",ts(eredm_sz,köznev),"=", end=" " )

if maradék:
	print( ts(eredm_sz//legnko, köznev//legnko) )
else:	
	print(eredm_sz//köznev)


#--- 7. feladat ---
#print("\n7. feladat:")
with open("adat.txt") as fbe, open("eredmeny.txt","w") as fki:
	for sor in fbe:
		sz1,n1,sz2,n2,művelet= sor.split()
		sz1,n1,sz2,n2 = int(sz1),int(n1),int(sz2),int(n2)
		if művelet=="*":
			eredm_sz=sz1*sz2
			eredm_n=n1*n2
			fki.write( ts(sz1,n1)+" * "+ts(sz2,n2)+" = "+ts(eredm_sz,eredm_n)+" = " )
			
		else: #"+"
			eredm_n= lkkt(n1,n2)
			tag1_sz= sz1*eredm_n//n1
			tag2_sz= sz2*eredm_n//n2
			eredm_sz= tag1_sz+tag2_sz
			fki.write( ts(sz1,n1)+" + "+ts(sz2,n2)+" = "+ts(tag1_sz,eredm_n)+" + "+ts(tag2_sz,eredm_n)+" = "+  ts(eredm_sz,eredm_n)+" = ")

		maradék= eredm_sz % eredm_n
		if maradék:
			legnko= lnko(eredm_sz,eredm_n)
			fki.write( ts(eredm_sz//legnko, eredm_n//legnko) )
		else:	
			fki.write( str(eredm_sz//eredm_n) )

		fki.write("\n")
		
#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben


