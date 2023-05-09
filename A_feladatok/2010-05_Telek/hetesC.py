#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# hetesC.py
# Érettségi feladat: 2010. május, Telek
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2016
#________________________________
# A 7. FELADAT EGY ÚJ VÁLTOZATA
#________________________________

#--- 1. feladat ---
#print("\n1. feladat:")

Gtelkek=[]	# páratlan házszámok
Jtelkek=[]	# párosak
with open("telkek.txt") as ff:
	darab= next(ff)
	for sor in ff:
		sor= sor.split()
		#if len(sor)!=3:
		#	continue
		házszám,szélesség,hosszúság= int(sor[0]),int(sor[1]),int(sor[2])
		if házszám%2:
			Gtelkek.append( [házszám,szélesség,hosszúság] )
		else:
			Jtelkek.append( [házszám,szélesség,hosszúság] )

#--- 7. feladat ---
#print("\n7. feladat:")

Jtelkek.sort()
Gtelkek.sort()

távolság=0
for telek in Jtelkek:
	házszám,szélesség,hosszúság= telek
	telek.append(távolság)	
	távolság+= szélesség
	
távolság=0
for telek in Gtelkek:
	házszám,szélesség,hosszúság= telek
	telek.append(távolság)	
	távolság+= szélesség

# Lépegetünk-indexelgetünk:
with open("joletsorC.csv","w") as ff:

	gkezdő=	0
	for jtelek in Jtelkek:
		jházszám,jszélesség,jhosszúság,jtávolság= jtelek

		maxhossz=0
		for i in range(gkezdő,len(Gtelkek)):
			gházszám,gszélesség,ghosszúság,gtávolság= Gtelkek[i]
			if gtávolság<=jtávolság+jszélesség:
				if ghosszúság>maxhossz:
					maxhossz= ghosszúság
				if gtávolság==jtávolság+jszélesség:
					break	
				gkezdő+=1
			else:
				break
		gkezdő-=1		
		
		ff.write("{};{};{}\n".format(jházszám,jszélesség,70-maxhossz))


#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben


