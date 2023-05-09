#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# godor.py
# Érettségi feladat: 2021. május, Gödrök
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2022

fmélység= "melyseg.txt"
lmélység= []

#--- 1. feladat
with open(fmélység) as ff:

    for sor in ff:

        sor= sor.strip()
        if not sor:
            continue
        lmélység.append( int(sor))

print( f"1. feladat\nA fájl adatainak száma: {len(lmélység)}")


#--- 2. feladat
print( "\n2. feladat")
itáv= int( input( "Adjon meg egy távolságértéket! ")) -1     # A távolság az 1. métertől számítódik, de az index 0-tól
print( f"Ezen a helyen a felszín {lmélység[itáv]} méter mélyen van.")


#--- 3. feladat
print( "\n3. feladat")
érintetlen= 100 * lmélység.count(0) / len(lmélység)
print( f"Az érintetlen terület aránya {érintetlen:.2f}%.")


#--- 4. feladat
fgödrök= "godrok.txt"

'''
# a) megoldás
with open( fgödrök, "w") as ff:

    gödörben= False
    első_sor= True
    for m in lmélység:

        if m == 0:
            gödörben= False
            continue

        if not gödörben:

            gödörben= True
            if első_sor:
                ff.write( f"{m} ")
                első_sor= False
            else:
                ff.write( f"\n{m} ")
        else:
            ff.write( f"{m} ")
'''

# b) megoldás
glist= [ ]
gödörben= False

for m in lmélység:

    if m == 0:
        gödörben= False
        continue

    ms= str(m)
    if not gödörben:
        gödörben= True
        glist.append( [ ms ])   # egy új gödröt kezdünk rögzíteni az első mélységi értékkel
    else:
        glist[-1].append( ms)   # az aktuális gödörhöz ( a glist-beli utolsóhoz) rögzítünk egy új értéket

with open( fgödrök, "w") as ff:

    glist= [ " ".join(s) for s in glist ]
    ff.write( "\n".join( glist))


#--- 5. feladat
print( f"\n5. feladat\nA gödrök száma: {len( glist)}")

#--- 6. feladat
print( "\n6. feladat")

if lmélység[ itáv] == 0:
    print( "Az adott helyen nincs gödör.")
else:
    kp= 0
    vp= len( lmélység) - 1

    for i in range( itáv, -1, -1):
        if lmélység[i] == 0:
            kp= i+1
            break

    for i in range( itáv+1, len( lmélység)):
        if lmélység[i] == 0:
            vp= i-1
            break

    # A kiírásnál 1-től sorszámozva adjuk meg a pozíciókat:
    print( f"a)\nA gödör kezdete: {kp+1} méter, a gödör vége: {vp+1} méter.")

d= 0
váltások= 0
for i in range( kp+1, vp+1):

    d1= lmélység[i] - lmélység[i-1]
    if d1 == 0:
        continue
    if d1 * d < 0:
        váltások += 1
    d= d1

if( váltások > 1):
    print( "b)\nNem mélyül folyamatosan.")
else:
    print( "b)\nFolyamatosan mélyül.")

print( f"c)\nA legnagyobb mélysége { max( lmélység[ kp : vp+1])} méter.")

térfogat= 10 * sum( lmélység[ kp : vp+1] )   # 10m * 1m * sum(mélységek)
print( f"d)\nA térfogata { térfogat} m^3.")

print( f"e)\nA vízmennyiség { térfogat - 10*( vp-kp +1 ) } m^3.")

#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben
