#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# hetesB.py
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

# A Gtelkeket 1 méteres telkekre osztjuk, és így a Jtelkekben lévő távolságokkal indexelni tudjuk őket.
# Elegendő lesz csak a hosszúságot tárolni:
Gsávok=[]	
for telek in Gtelkek:
	házszám,szélesség,hosszúság= telek
	Gsávok.extend( [hosszúság]*szélesség )

Gsávok.append(0) # lehessen túlindexelni a végén

with open("joletsorB.csv","w") as ff:

	jházszám,jszélesség,jhosszúság,jtávolság= Jtelkek[0]
	hosszak= Gsávok[0 : jtávolság+jszélesség+1]	# listaszeleteléssel
	ff.write("{};{};{}\n".format(jházszám,jszélesség,70-max(hosszak)))
	
	for i in range(1,len(Jtelkek)):
		jházszám,jszélesség,jhosszúság,jtávolság= Jtelkek[i]
		hosszak= Gsávok[jtávolság-1 : jtávolság+jszélesség+1] # listaszeleteléssel
		ff.write("{};{};{}\n".format(jházszám,jszélesség,70-max(hosszak)))


# Itt nem használunk listaszeletelést:
#
#with open("joletsorB.csv","w") as ff:
#
#	jházszám,jszélesség,jhosszúság,jtávolság= Jtelkek[0]
#	hosszak=[]
#	for i in range( jtávolság+jszélesség+1 ):
#		hosszak.append( Gsávok[i])
#	ff.write("{};{};{}\n".format(jházszám,jszélesség,70-max(hosszak)))
#
#	for i in range(1,len(Jtelkek)):
#		jházszám,jszélesség,jhosszúság,jtávolság= Jtelkek[i]
#		hosszak=[]
#		for i in range( jtávolság-1, jtávolság+jszélesség+1 ):
#			hosszak.append( Gsávok[i])
#		ff.write("{};{};{}\n".format(jházszám,jszélesség,70-max(hosszak)))
	

#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben


