#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# telefon.py
# Érettségi feladat: 2016. október, Telefonos ügyfélszolgálat
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2016

#--- 1. feladat ---
#print("\n1. feladat")
def mpbe(óra,perc,mp):
	return óra*3600+perc*60+mp
	
#--- 2. feladat ---
#print("\n2. feladat")
hívások=[]
sorszám=0
with open("hivas.txt") as ff:
	for sor in ff:
		sorszám+=1
		idők= [ int(e) for e in sor.split() ]
		hívások.append( [sorszám, mpbe(*idők[:3]), mpbe(*idők[3:]) ] )	# a '*' szétbontja a listát
		
#--- 3. feladat ---
print("\n3. feladat")
statisztika=[0 for i in range(24)]
for sorszám,kezdet,vég in hívások:		
	statisztika[kezdet//3600]+=1

for index,db in enumerate(statisztika):
	if db:
		print(index,"óra", db,"hívás")
	
#--- 4. feladat ---
print("\n4. feladat")

def hasonlítandó(tétel):
	sorszám,kezdet,vég= tétel	# return tétel[2]-tétel[1]
	return vég-kezdet			

sorszám,kezdet,vég= max( hívások,key=hasonlítandó)	# max(hívások,key=lambda tétel: tétel[2]-tétel[1])
tartam= vég-kezdet
print("A leghosszabb ideig vonalban lévő hívó a(z) {}. sorban szerepel, a hívás hossza: {} másodperc.".format(sorszám,tartam))

#--- 5. feladat ---
print("\n5. feladat")
óra,perc,másodperc= input("Adjon meg egy időpontot! (óra perc másodperc) ").split()
időpont= mpbe(int(óra),int(perc),int(másodperc))

hívó_sorszáma=None
várakozók=0
for sorszám,kezdet,vég in hívások:
	
	if kezdet<= időpont <= vég:
		várakozók+=1
		if not hívó_sorszáma:		# csak az első kell, a többi várakozik
			hívó_sorszáma= sorszám
			várakozók-=1


if hívó_sorszáma:
	print("A várakozók száma: {}, a beszélő a(z) {}. hívó.".format(várakozók,hívó_sorszáma) )
else:	
	print("Nem volt beszélő.")

#--- 6. feladat ---
print("\n6. feladat")
fogadottak=[]		# jó lesz a 7. feladathoz is,[ [sorszám, beszélgetés_kezdete, beszélgetés_vége, várakozás], ... ]
bkezdet= mpbe(8,0,0)	
bvég= mpbe(8,0,0)

for sorszám,hkezdet,hvég in hívások:

	if hvég//3600 < 8:		# a munkaidő kezdete előtt letették
		continue
	if hkezdet//3600 >= 12:	# a munkaidőn túl kezdték; ezeket már nem fogadják
		break				# 	a többit már nem kell vizsgálni
	if hvég <= bvég:		# a hívó letette mielőtt az előző beszélgetés befejeződött volna;
		continue						

	if hkezdet <= bvég:
		várakozás= bvég-hkezdet
		bkezdet= bvég
	else:
		várakozás=0
		bkezdet= hkezdet	

	bvég= hvég
	fogadottak.append( [sorszám,bkezdet,bvég,várakozás] )
	
print("Az utolsó telefonáló adatai a(z) {}. sorban vannak, {} másodpercig várt.".format(fogadottak[-1][0], fogadottak[-1][-1] ))

#--- 7. feladat ---
print("\n7. feladat")

def ópm(mp):
	return mp//3600, (mp//60)%60 ,mp%60

with open("sikeres.txt","w") as ff:
	
	for sorszám,bkezdet,bvég,várakozás in fogadottak:

		kó,kp,kmp= ópm(bkezdet)
		bó,bp,bmp= ópm(bvég)
		ff.write( "{} {} {} {} {} {} {}\n".format(sorszám,kó,kp,kmp,bó,bp,bmp) )

#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben

