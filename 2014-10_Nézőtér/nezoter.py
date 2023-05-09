#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# nezoter.py,
# Érettségi feladat: 2014. október, Nézőtér
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2016

#--- 1. feladat ---
#print("\n1. feladat")
# Így tároljuk az adatokat:
# nézőtér=[ sor1,sor2,... ]; sor=[ szék1,szék2,...]; szék=[foglaltság,kategória]
nézőtér=[]
with open("foglaltsag.txt") as ffog, open("kategoria.txt") as fkat:

	for fog_sor in ffog:
		fog_sor=fog_sor.strip()
		kat_sor= next(fkat).strip()
		nézőtér.append( [ [fog_sor[i],kat_sor[i]] for i in range(len(fog_sor))] )

#for sor in nézőtér:
#	print(sor)

#--- 2. feladat ---
print("\n2. feladat")
megadott_sor= int(input("Adja meg egy sor számát! "))
megadott_szék= int(input("Adja meg egy szék számát! "))

szék= nézőtér[megadott_sor-1][megadott_szék-1]
print("{}. sor {}. szék: {}".format(megadott_sor,megadott_szék,"foglalt" if szék[0]=="x" else "szabad") )

#--- 3. feladat ---
print("\n3. feladat")
székek_száma=0
foglaltak=0
for sor in nézőtér:
	székek_száma+= len(sor)
	for szék in sor:
		if szék[0]=="x":
			foglaltak+= 1
	
print("Az előadásra eddig {} jegyet adtak el, ez a nézőtér {}%-a.".format( foglaltak, round(foglaltak/székek_száma*100)) )

#--- 4. feladat ---
print("\n4. feladat")
katstat= dict()		# {kategória:darab} statisztika az eladott jegyek kategóriáira
for sor in nézőtér:
	for szék in sor:
		if szék[0]=="x":
			kategória= szék[1]
			katstat[kategória]= katstat.get(kategória,0)+1

legtöbb= max(katstat.values())
for kategória,darab in katstat.items():	# több kategóriában is eladhattak ugyanolyan sok jegyet
	if darab==legtöbb:
		print("A legtöbb jegyet a(z) {}. árkategóriában értékesítették.".format(kategória) )

#--- 5. feladat ---
print("\n5. feladat")
árak=(5000,4000,3000,2000,1500)
bevétel=0
for kategória,darab in katstat.items():
	bevétel+= árak[int(kategória)-1]*darab

print("A színház bevétele:",bevétel,"Ft")

#--- 6. feladat ---
print("\n6. feladat")
egyedüliek=0

for sor in nézőtér:
	üres_szakasz=0
	for szék in sor:
		if szék[0]=="o":
			üres_szakasz+=1
		else: # "x": lezárja az üresek sorozatát
			if üres_szakasz==1:
				egyedüliek+=1
			üres_szakasz=0
	if üres_szakasz==1:	# a sor végén is vizsgálni kell
			egyedüliek+=1
			
print("Az egyedülálló helyek száma:", egyedüliek)

#--- 7. feladat ---
#print("\n7. feladat")
with open("szabad.txt","w") as ff:
	for sor in nézőtér:
		for szék in sor:
			ff.write( szék[1] if szék[0]=="o" else "x")
		ff.write("\n")
		
#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben


