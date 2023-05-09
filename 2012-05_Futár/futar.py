#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# futar.py
# Érettségi feladat: 2012. május, Futár
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2016

#--- 1. feladat ---
#print("\n1. feladat:")
útnapló=[]
with open("tavok.txt") as ff:
	for sor in ff:
		nap,sorszám,táv= sor.split()
		útnapló.append( (int(nap),int(sorszám),int(táv)) )

# Rendezzük a listát, az első kulcs a nap száma, a második az út napon belüli sorszáma stb.
útnapló.sort()
#print(útnapló)

#--- 2. feladat ---
print("\n2. feladat:")
print("A hét legelső útja {} km volt.".format(útnapló[0][2]))

#--- 3. feladat ---
print("\n3. feladat:")
print("A hét legutolsó útja {} km volt.".format(útnapló[-1][2]))

#--- 4. feladat ---
print("\n4. feladat:")
napok= [0]*8
for nap,sorszám,táv in útnapló:
	napok[nap]+=1

print("Ezeken a napokon nem dolgozott:",end=" ")
for i in range(1,8):
	if napok[i]==0:
		print(i,end=" ")	
print()

#--- 5. feladat ---
print("\n5. feladat:")
legtöbb= max(napok)
print("A legtöbb fuvar napja(i):",end=" ")
for i in range(1,8):
	if napok[i]==legtöbb:
		print(i,end=" ")
print()		

#--- 6. feladat ---
print("\n6. feladat:")
távok=[0]*8
for nap,sorszám,táv in útnapló:
	távok[nap]+=táv

for i in range(1,8):
	print("{}. nap: {} km".format(i,távok[i]))	

#--- 7. feladat ---
print("\n7. feladat:")

def díjazás(táv):
	díj=0
	if táv<=2:
		díj=500
	elif táv<=5:
		díj=700
	elif táv<=10:
		díj=900
	elif táv<=20:
		díj=1400
	else:
		díj=2000
	return díj

megadott_táv=input("Adjon meg egy távolságot (1 - 30 km): ")
print("A távolság díjazása:", díjazás(int(megadott_táv)))

#--- 8. feladat ---
#print("\n8. feladat:")
heti_kereset=0
with open("dijazas.txt","w") as ff:
	for nap,sorszám,táv in útnapló:
		díj= díjazás(táv)
		ff.write("{}. nap {}. út: {} Ft\n".format(nap,sorszám,díj))
		heti_kereset+= díj
		
#--- 9. feladat ---
print("\n9. feladat:")
#print("A heti kereset:",heti_kereset,"Ft")
print("A heti kereset: {0:,} Ft".format(heti_kereset) )

#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben


