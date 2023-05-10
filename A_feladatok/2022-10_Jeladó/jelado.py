#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# jelado.py
# Érettségi feladat: 2022. október, Jeladó
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2023

import math     # math.sqrt

#--- 1. feladat
jelek= []

with open("jel.txt") as ff:

    for sor in ff:

        sor= sor.strip()
        if not sor:
            continue

        jelek.append( [ int(v) for v in sor.split() ]  )

# print( *jelek, sep="\n")


#--- 2. feladat
print("\n2. feladat")
sorszám= int( input( "Adja meg a jel sorszámát! ") ) - 1
print( f"x={ jelek[sorszám][3]} y={ jelek[sorszám][4]}")


#--- 3. feladat
def eltelt( t1, t2):
    """
    t1 és t2 olyan legalább háromelemű indexelhető objektum,
    amelynek első elemei az óra, perc, mp értékek.
    """
    dtime= t1[0]*3600 + t1[1] * 60 + t1[2]  - t2[0]*3600 - t2[1] * 60 - t2[2]
    return dtime if dtime >= 0 else -dtime


#--- 4. feladat
ttime= eltelt( jelek[0][:4], jelek[-1][:4] )
print( f"\n4. feladat\nIdőtartam: {ttime//3600}:{ttime%3600//60}:{ttime%60}" )


#--- 5. feladat
# A 'jelek' listának az az eleme (ami [ó,p,mp,x,y] formájú lista), ahol az x a legkisebb:
bejegyzés1= min( jelek, key= lambda l: l[3] )
# print( bejegyzés1)
x1= bejegyzés1[3]
# Nem részletezve:
x2= max( jelek, key= lambda l: l[3] )[3]
y1= min( jelek, key= lambda l: l[4] )[4]
y2= max( jelek, key= lambda l: l[4] )[4]

print( f"\n5. feladat\nBal alsó: {x1} {y1}, jobb felső: {x2} {y2}")


#--- 6. feladat
elmozdulás= 0

for i in range( 1, len(jelek)):
    elmozdulás += math.sqrt( (jelek[i-1][3] - jelek[i][3]) ** 2 + (jelek[i-1][4] - jelek[i][4]) ** 2 )

print( f"\n6. feladat\nElmozdulás: {elmozdulás:.3f} egység")


#--- 7. feladat

with open("kimaradt.txt", "w") as ff:

    for i in range( 1, len(jelek)):

        dx= abs( jelek[i][3] - jelek[i-1][3] )
        dy= abs( jelek[i][4] - jelek[i-1][4] )
        dt= eltelt( jelek[i], jelek[i-1])

        ndxy= ( max( dx,dy) -1 ) // 10
        ndt= ( dt -1) // 300    # 5 perc == 300 mp

        if ndxy > 0 or ndt > 0 :

            ff.write( f"{jelek[i][0]} {jelek[i][1]} {jelek[i][2]}")

            if( ndt > ndxy):
                ff.write( f" időeltérés {ndt}\n")
            else:
                ff.write( f" koordináta-eltérés {ndxy}\n")


#---------------------------------------------------------------------------
# További feladatok: https://github.com/kantal/kozepiskolai_inf_feladatok
# Ajánlott könyv:    Koós Antal: Python a gépben
