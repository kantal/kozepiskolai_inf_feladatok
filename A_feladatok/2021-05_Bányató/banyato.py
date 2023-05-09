#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# banyato.py
# Érettségi feladat: 2021. május, Bányató
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2022

# Megjegyzés a kerekítéshez: lásd a 6. feladatnál!

fmélység= "melyseg.txt"

#--- 1. feladat
térkép= []
felszín= 0
max_mély= (0,0,0)     # (mélység, sor, oszlop)

with open( fmélység) as ff:

    next(ff)    # átugorjuk az első két sort
    next(ff)

    összmély= 0
    sorindex= -1
    for sor in ff:

        sor= sor.strip()
        if not sor:     # az esetleges üres sorokat átugorjuk
            continue

        sorindex += 1
        sor_mély= []
        for oszlop, mélység in enumerate( sor.split()):

            mélység= int( mélység)
            sor_mély.append( mélység)
            if mélység != 0:

                felszín += 1
                összmély += mélység
                if max_mély[0] < mélység:
                    max_mély= ( mélység, sorindex, oszlop)

        térkép.append( sor_mély)

#--- 2. feladat
print( "\n2. feladat")
bekért_sor= int( input( "A mérés sorának azonosítója="))
bekért_oszlop= int( input( "A mérés oszlopának azonosítója="))
print( f"A mért mélység az adott helyen { térkép[ bekért_sor-1][ bekért_oszlop-1]} dm")


#--- 3. feladat
átlag_mélység= összmély / (felszín * 10)   # m
print( f"\n3. feladat\nA tó felszíne: {felszín} m2, átlagos mélysége: {átlag_mélység:.2f} m")

#--- 4. feladat
print( f"\n4. feladat\nA tó legnagyobb mélysége: {max_mély[0]} dm")
print( "A legmélyebb helyek sor-oszlop koordinátái:")
sn= len(térkép)
on= len( térkép[0])
print( *( f"({s+1};{o+1})" for s in range(sn) for o in range(on) if térkép[s][o] == max_mély[0] ), sep= "\t")

#--- 5. feladat
# Az első és utolsó sorok ill. oszlopok csak 0-át tartalmaznak, amit kihasználunk az indexelésnél.
partvonal= 0
for s in range(1,sn-1):
    for o in range(1,on-1):
        partvonal += sum( 1 for ds,do in ( (-1,0),(1,0),(0,-1),(0,1)) if térkép[s][o] and térkép[s+ds][o+do] == 0)

print( f"\n5. feladat\nA tó partvonala {partvonal} m hosszú")


#--- 6. feladat
"""
 Megjegyzés: A 6. feladatban a kiírás szerint a kerekítést a "matematika szabályainak megfelelően"
kell elvégezni. Ez valószínűleg azt jelenti, hogy például a 6.5-ös értéket 7-re kellene kerekíteni,
azaz felfelé. Azonban az Oktatási Hivatal által megoldásként adott diagram.txt-ben ez az érték
6-nak adódik, ami statisztikai kerekítés eredménye, azaz a feles érték a közelebbi páros egészre
módosul. Szerencsére a Python round() függvény is így működik.

Lehetőségek a feles érték felfelé kerekítéséhez:

int( v + 0.5)

    vagy univerzálisabban:

from decimal import *
v= Decimal( 6.5)
w= v.quantize( Decimal( "1."), ROUND_HALF_UP )      # --> 7
#w= v.quantize( Decimal( "1."), ROUND_HALF_EVEN )    # --> 6
w= int(w)
#w= float(w)
print(w)

"""

print( "\n6. feladat")
voszlop= int( input( "A vizsgált szelvény oszlopának azonosítója=")) -1
fdiagram= "diagram.txt"

with open( fdiagram,"w") as ff:

    for s in range(sn):

        csillagok= round( térkép[s][voszlop]/10) * "*"
        ff.write( f"{s+1:02}{csillagok}\n")

#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben
