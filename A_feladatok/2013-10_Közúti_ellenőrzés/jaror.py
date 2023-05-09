#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# jaror.py,
# Érettségi feladat: 2013. október, Közúti ellenőrzés
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2016

#--- 1. feladat ---
#print("\n1. feladat:")
járművek=[]
with open("jarmu.txt") as ff:
	for sor in ff:
		óra,perc,mp,rendszám= sor.split()
		járművek.append( (int(óra),int(perc),int(mp),rendszám) )
#print(járművek)		

#--- 2. feladat ---
print("\n2. feladat:")
print("A rendőrök legalább", járművek[-1][0]+1 - járművek[0][0],"órát dolgoztak.")

#--- 3. feladat ---
print("\n3. feladat:")
print("Műszaki ellenőrzésen átesett járművek:")
vizsgaidő= None	# a vizsgálat órája
for óra,perc,mp,rendszám in járművek:
	if óra!=vizsgaidő:
		print(óra,"óra:",rendszám)
		vizsgaidő=óra

#--- 4. feladat ---
print("\n4. feladat:")
buszok,motorok,kamionok,szgk=0,0,0,0
for óra,perc,mp,rendszám in járművek:
	betűjel= rendszám[0]
	if betűjel=="B":
		buszok+=1
	elif betűjel=="M":
		motorok+=1
	elif betűjel=="K":
		kamionok+=1
	else:
		szgk+=1

print("Buszok:",buszok,"\nMotorok:",motorok,"\nKamionok:",kamionok,"\nSzemélygépkocsik:",szgk)

#--- 5. feladat ---
print("\n5. feladat:")

def idődiff( kezdő,végső ):	
# input: kezdő időpont, végső időpont
# return: a különbözet mp-ben
	kó,kp,kmp=kezdő
	vó,vp,vmp=végső
	return vó*3600+vp*60+vmp-kó*3600-kp*60-kmp

hossz=0
kezdő_index= None
for i in range(1,len(járművek)):
	időszak= idődiff( járművek[i-1][:3], járművek[i][:3] )
	if időszak>hossz:
		hossz=időszak
		kezdő_index= i-1

kezdete= járművek[kezdő_index]
vége= járművek[kezdő_index+1]

print("A leghosszabb forgalommentes időszak: {}:{}:{}-{}:{}:{}".format( *(kezdete[:3]+vége[:3]) ))
#print("A leghosszabb forgalommentes időszak: {}:{}:{}-{}:{}:{}".format( kezdete[0],kezdete[1],kezdete[2],vége[0],vége[1],vége[2]))


#--- 6. feladat ---
print("\n6. feladat:")
keresett= input("Adja meg a keresett rendszámot, az ismeretlen karaktereket *-gal jelölje! ").upper()
if len(keresett)!=7:
	print("A rendszámban 7 karakternek kell lennie!")
	exit(1)

találtak=[]
for óra,perc,mp,rendszám in járművek:
		for i in range(len(keresett)):
			if keresett[i]!="*" and keresett[i]!=rendszám[i]:
				break
		else:		
			találtak.append(rendszám)

if találtak:
	print("Az illeszkedő rendszámok:")
	for rendszám in találtak:
		print(rendszám)
else:
	print("Nincs illeszkedő rendszám")
		
#--- 7. feladat ---
#print("\n7. feladat:")
with open("vizsgalt.txt","w") as ff:

	#ff.write("{0:02d} {1:02d} {2:02d} {3}\n".format(járművek[0][0],járművek[0][1],járművek[0][2],járművek[0][3]) )
	ff.write("{0:02d} {1:02d} {2:02d} {3}\n".format( *járművek[0]) )
	vizsgált= járművek[0]
	for i in range(1,len(járművek)):
		if idődiff(vizsgált[:3],járművek[i][:3])>=5*60 :
			ff.write("{0:02d} {1:02d} {2:02d} {3}\n".format( *járművek[i]) )
			vizsgált=járművek[i]

#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben


