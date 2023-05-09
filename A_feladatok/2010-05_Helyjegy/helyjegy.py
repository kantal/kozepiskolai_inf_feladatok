#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# helyjegy.py
# Érettségi feladat: 2010. május, Helyjegy
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2016

#--- 1. feladat ---
#print("\n1. feladat:")
jegyek=[]
with open("eladott.txt") as ff:

	jegyek_száma,járathossz,szakaszár= next(ff).split()
	jegyek_száma,járathossz,szakaszár= int(jegyek_száma),int(járathossz),int(szakaszár)
	for sor in ff:
		sor= sor.split()
		if len(sor)==3:
			ülés,felszállás,leszállás= sor
			jegyek.append( (int(ülés),int(felszállás),int(leszállás)) )
		
#--- 2. feladat ---
print("\n2. feladat: A legutolsó vásárló ülése {}, a leutazott távolság {} km.".format(jegyek[-1][0],jegyek[-1][2]-jegyek[-1][1]) )

#--- 3. feladat ---
végig_utazók= [ str(index+1) for index,(ülés,felszállás,leszállás) in enumerate(jegyek) if felszállás==0 and leszállás==járathossz ]

print("\n3. feladat: A végig utazók sorszáma:", " ".join(végig_utazók))

#--- 4. feladat ---
kerekítés=[0,-1,-2, 2, 1, 0, -1,-2, 2,1]

def díj(tétel):
	ülés,felszállás,leszállás= tétel
	táv= leszállás-felszállás
	összeg= táv//10*szakaszár
	if táv%10:
		összeg+= szakaszár
		
	return összeg + kerekítés[ összeg%10 ]

bevétel=0
for tétel in jegyek:
	bevétel+= díj(tétel)

print("\n4. feladat: A bevétel {} Ft.".format(bevétel))

#--- 5. feladat ---

def hasonlítandó( tétel):
	ülés,felszállás,leszállás=tétel
	# A végállomás távolságát 0-nak vesszük, hogy a keresésbe ne "zavarjon be".
	if leszállás==járathossz:
		leszállás=0
	return max(leszállás,felszállás)	

ül,felsz,uelőtti = max( jegyek,key=hasonlítandó)

le,fel=0,0
for ülés,felszállás,leszállás in jegyek:
	if leszállás==uelőtti:
		le+=1
	elif felszállás==uelőtti:
		fel+=1
	
print("\n5. feladat: Az utolsó előtti megállóban ({} km) {} utas szállt le, illetve {} fel, összesen {}.".format(uelőtti,le,fel,le+fel))

#--- 6. feladat ---
megállók= set()
for ülés,felszállás,leszállás in jegyek:
	megállók.add(felszállás)
	megállók.add(leszállás)

print("\n6. feladat: A busz {} közbenső helyen állt meg.".format(len(megállók)-2) )

#--- 7. feladat ---
táv= int(input("\n7. feladat: Adja meg, hogy az út mely kilométerén kéri az utaslistát! "))
ülések=[0]*48
for index,(ülés,felszállás,leszállás) in enumerate(jegyek):
	if 	felszállás<= táv <leszállás:
		ülések[ülés-1]=index+1

with open("kihol.txt","w") as ff:
	for index in range(48):
		if ülések[index]==0:
			ff.write("{}. ülés: üres\n".format(index+1))
		else:
			ff.write("{}. ülés: {}. utas\n".format(index+1,ülések[index]))	
		

#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben


