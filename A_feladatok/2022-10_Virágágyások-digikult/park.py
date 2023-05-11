#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# park.py
# Érettségi feladat - digitális kultúra, emelt szint: 2022. október, Virágágyások
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2023

#--- 1. feladat
Aj= []      # felajánlások; az elemei ( intervallum, szín) vagy ( [interv1, interv2], szín)
with open("felajanlas.txt") as ff:

    Nágy= int( next(ff))
    for sor in ff:

        sor= sor.strip()
        if not sor:
            continue

        a,b,szín= sor.split()
        a= int(a)
        b= int(b)
        if a <= b:
            t= ( range(a,b+1), szín )
        else:
            t= ( [range(a,Nágy+1),range(1,b+1)], szín )

        Aj.append(t)

#print( *Aj, sep="\n")   # szemrevételezés


#--- 2. feladat
print( f"\n2. feladat\nA felajánlások száma: {len(Aj)}")


#--- 3. feladat
kétoldaliak= [ index for index,ajánlás in enumerate(Aj,1) if len( ajánlás[0]) == 2 ]
print( "\n3. feladat\nA bejárat mindkét oldalán ültetők:", *kétoldaliak )


#--- 4. feladat
bekért_sorszám= int( input( "\n4. feladat\nAdja meg az ágyás sorszámát! "))     # 1-től kezdődik


def get_felajánlások( ágy_sorszám):
    # Az adott ágyásra vonatkozó felajánlások sorszámainak listája lesz a visszatérési érték.
    l= []
    for index, (interv, szín) in enumerate( Aj,1):

        if type(interv) == range:
            if ágy_sorszám in interv:
                l.append( index)

        else: # [range, range]
            if ágy_sorszám in interv[0]  or  ágy_sorszám in interv[1]:
                l.append( index)

    return l


l_felaj= get_felajánlások( bekért_sorszám)
print( f"A felajánlók száma: {len(l_felaj)}")

if l_felaj:

    színek= [ Aj[sorszám-1][1] for sorszám in l_felaj ]
    print( f"A virágágyás színe, ha csak az első ültet: {színek[0]}")
    print( "A virágágyás színei:", *set(színek) )
else:
    print( "Ezt az ágyást nem ültetik be.")


#--- 5 - 6. feladat
n_vállalt_ágyások= 0
n_felajánlottak= 0

with open("szinek.txt","w") as ff:

    for ágy_sorszám in range( 1, Nágy+1):

        l_felaj= get_felajánlások( ágy_sorszám)
        if l_felaj:

            n_vállalt_ágyások += 1
            sorszám= l_felaj[0]
            interv, szín = Aj[ sorszám -1 ]

            ff.write( f"{szín} {sorszám}\n")

            n_felajánlottak += len( l_felaj)

        else:
            ff.write( "# 0\n")

print("\n5. feladat")
if n_vállalt_ágyások == Nágy:
    print("Minden ágyás beültetésére van jelentkező.")
elif n_felajánlottak >= Nágy:
    print("Átszervezéssel megoldható a beültetés.")
else:
    print("A beültetés nem oldható meg.")


#---------------------------------------------------------------------------
# További feladatok: https://github.com/kantal/kozepiskolai_inf_feladatok
# Ajánlott könyv:    Koós Antal: Python a gépben
