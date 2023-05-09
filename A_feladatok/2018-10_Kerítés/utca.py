#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# utca.py
# Érettségi feladat: 2018. október, Kerítés
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2018

#--- 1. feladat ---
utca=[[],[]]    # páros, páratlan oldalak
with open("kerites.txt") as ff:

    for sor in ff:
        sor=sor.strip()
        if not sor:
            continue
        paritás,szélesség,szín= sor.split()
        paritás,szélesség=int(paritás),int(szélesség)
        utca[paritás].append( (szélesség,szín) )

#--- 2. feladat ---
print("2. feladat\nAz eladott telkek száma: {}\n".format(len(utca[0])+len(utca[1])) )

#--- 3. feladat ---
if paritás==0:
    oldal= "páros"
    házszám= len(utca[0])*2
else:
    oldal= "páratlan"
    házszám= 2*len(utca[1])-1

print("3. feladat\nA {} oldalon adták el az utolsó telket.\nAz utolsó telek házszáma: {}\n".format(oldal,házszám) )

#--- 4. feladat ---
upáratlan= utca[1]
szín= upáratlan[0][1]
for index in range(1,len(upáratlan)):

    szín2=upáratlan[index][1]
    if szín not in "#:" and szín==szín2:
        # A lista első elemének indexe 0, ezért az indexből a páratlan házszám így kapható: 2*index+1
        előző_házszám= 2*(index-1)+1    
        print("4. feladat\nA szomszédossal egyezik a kerítés színe: {}\n".format(előző_házszám))
        break
    szín=szín2
        
#--- 5. feladat ---
mhsz= int( input("5. feladat\nAdjon meg egy házszámot! ") )

# Házszámból index:
# hszptlan=2*index+1 --> index=(hszptlan-1)/2
# hszps=2*(index+1)  --> index=hszps/2-1

pari= mhsz%2
oldal= utca[pari]
index= (mhsz-1)//2 if pari else mhsz//2-1
szélesség,szín= oldal[index]
meglévő_színek= [szín]
if index-1>=0:
    meglévő_színek.append( oldal[index-1][1] )
if index+1 < len(oldal):
    meglévő_színek.append( oldal[index+1][1] ) 

# Legfeljebb 3 tiltott szín van, a saját és a maximum két szomszédé.
# Így bármely négy különböző színből valamelyik megfelelő lesz.
for új_szín in "ABCD":
    
    if új_szín not in meglévő_színek:
        break

print("A kerítés színe / állapota: {}\nEgy lehetséges festési szín: {}".format(szín,új_szín))

#--- 6. feladat ---
with open("utcakep.txt","w") as ff:

    sor2=""
    for index,(szélesség,szín) in enumerate(utca[1]):
        sor2= sor2 + str(2*index+1).ljust(szélesség)    # páratlan házszám
        ff.write(szélesség*szín)
        
    ff.write("\n")    
    ff.write(sor2)

#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben

