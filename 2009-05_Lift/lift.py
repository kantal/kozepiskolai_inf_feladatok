#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# lift.py
# Érettségi feladat: 2009. május, Lift
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2016

#--- 1. feladat ---
print("\n1. feladat")

with open("igeny.txt") as ff:
	szintek_száma= int(next(ff))
	csapatok_száma= int(next(ff))
	igények_száma= int(next(ff))

	igények=[]
	for sor in ff:
		óra,perc,mp,csapat,indszint,célszint= [ int(e) for e in sor.split() ]
		igények.append( [óra,perc,mp, csapat,indszint,célszint] )
		#igények.append( [ int(e) for e in sor.split() ] )	# ezzel a fenti két sort helyettesíthetjük


#--- 2. feladat ---
startszint= int(input("\n2. feladat Kérem a lift indulási helyét (1-{}): ".format(szintek_száma)))

#--- 3. feladat ---
print("\n3. feladat")
print("A lift a {}. szinten áll az utolsó igény teljesítése után.".format( igények[-1][-1]) )

#--- 4. feladat ---
print("\n4. feladat")

legalacsonyabb,legmagasabb= startszint,startszint
for óra,perc,mp, csapat,indszint,célszint in igények:
	legalacsonyabb= min(legalacsonyabb,indszint,célszint)
	legmagasabb= max(legmagasabb,indszint,célszint)

print("A lift által érintett legalacsonyabb szint a(z) {}., a legmagasabb {}.".format(legalacsonyabb,legmagasabb))

#--- 5. feladat ---
print("\n5. feladat")
aktuális_szint= startszint
fel_utassal, fel_utas_nélkül= 0,0

for óra,perc,mp, csapat,indszint,célszint in igények:

	if aktuális_szint < indszint:
		fel_utas_nélkül+=1
	if indszint<célszint:
		fel_utassal+=1
	aktuális_szint= célszint

print("Felfelé a lift utassal {} alkalommal ment, utas nélkül {} alkalommal.".format(fel_utassal,fel_utas_nélkül))

#--- 6. feladat ---
print("\n6. feladat")
használat=[0]*(csapatok_száma+1)	# A 0-ás indexet nem fogjuk használni.
for óra,perc,mp, csapat,indszint,célszint in igények:
	használat[csapat]+=1

print("A liftet nem vették igénybe a következő csapatok:",end=" ")
for cs in range(1,len(használat)):
	if not használat[cs]:
		print(cs,end=" ")
print()		

#--- 7. feladat ---
print("\n7. feladat")
import random
random.seed()
csapodár= random.randrange(1,csapatok_száma+1)
#csapodár=3
#csapodár=19

szint=None
gyalog=[]
for óra,perc,mp, csapat,indszint,célszint in igények:

	if csapat!=csapodár:
		continue
		
	if not szint:
		szint=célszint	# az első liftezéskor
		continue

	if szint!=indszint:
		gyalog.append( (szint,indszint))

	szint= célszint

if gyalog:
	print("A {}. sz. csapat a következő szintek között gyalog ment:".format(csapodár),end=" ")
	for sz1,sz2	in gyalog:
		print("{}-->{}".format(sz1,sz2),end=" ")
	print()
else:
	print("A {}. sz. csapatról: Nem bizonyítható szabálytalanság.".format(csapodár))

#--- 8. feladat ---
print("\n8. feladat")

with open("blokkol.txt","w") as ff:

	infó= "A {}. csapat által végzett munkák kimutatása\n".format(csapodár)
	s_emelet= "Indulási emelet: {}\nCélemelet: {}"
	s_befejezés= "Befejezés ideje: {}:{}:{}"

	print(infó)
	ff.write(infó+"\n")
	
	for óra,perc,mp, csapat,indszint,célszint in igények:

		if csapat==csapodár:

			s= s_befejezés.format(óra,perc,mp)
			print(s)
			ff.write(s+"\n")

			siker= int(input("Adja meg a sikerességet(0:befejezetlen, 1:befejezett): "))
			ff.write("Sikeresség: "+("befejezetlen" if not siker else "befejezett") +"\n-----\n")
			print("-----")
			s= s_emelet.format(indszint,célszint)
			print(s)
			ff.write(s+"\n")
			
			ff.write("Feladatkód: " +input("Adja meg a feladatkódot(1-99): ") +"\n")

#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben


