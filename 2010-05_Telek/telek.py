#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# telek.py
# Érettségi feladat: 2010. május, Telek
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2016

#--- 1. feladat ---
#print("\n1. feladat:")

Gtelkek=[]	# páratlan házszámok
Jtelkek=[]	# párosak
with open("telkek.txt") as ff:
	darab= next(ff)
	for sor in ff:
		sor= sor.split()
		#if not sor or len(sor)!=3:
		#	continue
		házszám,szélesség,hosszúság= int(sor[0]),int(sor[1]),int(sor[2])
		if házszám%2:
			Gtelkek.append( [házszám,szélesség,hosszúság] )
		else:
			Jtelkek.append( [házszám,szélesség,hosszúság] )

#--- 2. feladat ---
print("\n2. feladat:")
Ghossz,Jhossz = 0,0
for házszám,szélesség,hosszúság in Gtelkek:
	Ghossz+= szélesség
for házszám,szélesség,hosszúság in Jtelkek:
	Jhossz+= szélesség

print("Gazdagsor {} m, Jólétsor {} m.".format(Ghossz,Jhossz))
print("A körbejárás hossza {} m".format(2*80+Ghossz+Jhossz))

#--- 3. feladat ---
print("\n3. feladat:")
keskeny_jólét=0
for házszám,szélesség,hosszúság in Jtelkek:
	if szélesség<=20:
		keskeny_jólét+=1
		
print("Jólétsoron a 20 méternél nem szélesebb telkek száma:",keskeny_jólét)		

#--- 4. feladat ---
print("\n4. feladat:")

min_gtelek= None
min_gterület= float("inf")	# Ennél biztos lesz kisebb :-)
#min_gtelek= Gtelkek[0]
#min_gterület= Gtelkek[0][1]*Gtelkek[0][2]

max_gtelek= None
max_gterület= 0

for telek in Gtelkek:
	házszám,szélesség,hosszúság= telek
	t= szélesség*hosszúság
	if t<min_gterület:
		min_gterület,min_gtelek= t,telek
		
	if t>max_gterület:
		max_gterület,max_gtelek= t,telek

print("Gazdagsor legkisebb és legnagyobb telke:")
print("\t házsz.:{}, terület: {}\n\t házsz.:{}, terület: {}".format(min_gtelek[0],min_gterület,max_gtelek[0],max_gterület))
print("\t Közöttük {} telek van.".format( abs(min_gtelek[0]-max_gtelek[0])//2-1 ) )
# Feltételeztük, hogy csak egyetlen minimális (vagy maximális) telek van.

#--- 5. feladat ---
print("\n5. feladat:")

def adó(telek):
	házszám,szélesség,hosszúság= telek
	terület= szélesség*hosszúság
	összeg=0
	
	if terület<=700:
		összeg+= terület*51
	elif terület<=1000:
		összeg+= 700*51+(terület-700)*39
	else:
		összeg+= 700*51+300*39+200

	if szélesség<=15 or hosszúság<=25:
		összeg-= összeg//5
	
	maradék= összeg%100
	if maradék>=50:
		összeg+=100-maradék
	else:
		összeg-=maradék	
	return összeg


bevétel=0
for telek in Gtelkek:
	bevétel+= adó(telek)
	
print("Gazdagsor után az adóbevétel {} Fabatka".format(bevétel))

#--- 6. feladat ---
print("\n6. feladat:")

Jtelkek.sort()	# Az elsődleges kulcs az első elem, azaz a házszám lesz, és ez nekünk így jó.

távolság=0
for telek in Jtelkek:
	házszám,szélesség,hosszúság= telek
	telek.append(távolság)	# ha kiszámoltuk, akkor hozzá is fűzzük a telek adataihoz
	távolság+= szélesség
	
print("Az utolsó három telek száma és távolsága Jólétsoron:")
for i in range(-1,-4,-1):
	print("\t{}, {}m".format( Jtelkek[i][0],Jtelkek[i][3]))

#vég=len(Jtelkek)-1
#for i in range(3):
#	print("\t{}, {}m".format( Jtelkek[vég-i][0],Jtelkek[vég-i][3]))	


#--- 7. feladat ---
#print("\n7. feladat:")

# A Gtelkekhez is hozzáfűzzük a távolságokat:
Gtelkek.sort()
távolság=0
for telek in Gtelkek:
	házszám,szélesség,hosszúság= telek
	telek.append(távolság)	
	távolság+= szélesség

# Ezen feladathoz több, máshol fellelhető megoldást is áttekintettem, s úgy találtam, hogy azok az optimális,
# kevés számolást igénylő megoldásra törekedve, olyan indexeléses és feltételes kifejezéseket használnak, amelyeket
# könnyű eltéveszteni. Sőt, volt olyan "tökéletes" megoldás, ami csak az érettségire adott telkek.txt-vel működött
# helyesen, de egy más adatokat tartalmazó tesztfájllal már nem.
# Érettségin kevés az idő, így az sem baj, ha néha nem optimálisan, esetleg nyers erővel oldunk meg feladatokat.
# Az alábbi megoldás például nem optimális, mert nem használja ki, hogy a telkek adatai sorba vannak rendezve az
# utca elejétől mért távolság szerint, és minden egyes "jtelek"-hez újra megvizsgálja az összes "gtelket".

with open("joletsor.csv","w") as ff:

	for jtelek in Jtelkek:
		jházszám,jszélesség,jhosszúság,jtávolság= jtelek

		szemben=[ ghosszúság for (gházszám,gszélesség,ghosszúság,gtávolság) in Gtelkek if jtávolság<= gtávolság <= jtávolság + jszélesség  or gtávolság<= jtávolság <= gtávolság+gszélesség ]
		
		ff.write("{};{};{}\n".format(jházszám,jszélesség,70-max(szemben)))


#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben


