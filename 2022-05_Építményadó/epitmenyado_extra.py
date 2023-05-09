#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# epitmenyado_extra.py
# Érettségi feladat: 2022. május, Építményadó
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2022

"""
 Az alapváltozattól való eltérések:

- az adatok beolvasásakor egy menetben töltjük fel a dict-eket;
- nem hagyatkozunk arra, hogy csak 3 adósáv van, lehetne akár len(string.ascii_uppercase) darab;
- egyéb, kisebb trükköket alkalmazunk.

"""

import string

fn_utca= "utca.txt"
fn_fizetendő= "fizetendo.txt"

lutca= []   # Az utca.txt adatai, plusz az ingatlanonként fizetendő adó.
sum_adósáv= dict()  # Az 5. feladathoz, pl. 'A' --> [ telkek száma, adóösszeg ]
utca_sávok= dict()  # A 6. feladathoz, utcanév --> set( ) a sávokkal
tulaj= dict()       # A 7. feladathoz, adószám --> szumma adó

#--- 4. feladat
adósávok= dict()    # pl. 'A' -> négyzetméterenkénti összeg

def adó( sáv, terület):
    """ Kiszámítja az egy ingatlan után fizetendő adót
    sáv: str
    terület: int
    Az 'adósávok' dict-et is használjuk, amit inicializálni szükséges a főprogramban.

    Return: int
    """
    összeg= adósávok[ sáv] * terület
    return  összeg if összeg >= 10_000 else 0


#--- 1., 5., 6., 7. feladatok

with  open( fn_utca) as ff:

    for sor in ff:

        sor= sor.strip()
        if not sor:
            continue        # az esetleges üres sorokat átugorjuk

        if not adósávok:
            """
            Még az 'adósávok' dict üres, ebből a sorból töltjük fel.
            Egy dict-et létrehozhatunk kételemű sokaságokból is, amelyekben az első elem
            lesz a kulcs, a második a hozzátartozó érték.
            A zip() két vagy több konténer elemeit két- vagy többelemű sokaságokba rendezi össze.
            """
            adósávok= dict( zip( string.ascii_uppercase, [ int(s) for s in sor.split()]) )

            #'''
            print("\n--- Ismerkedés")
            print( string.ascii_uppercase, sor.split(), sep="\n")
            print()
            print( string.ascii_uppercase, [ int(s) for s in sor.split()], sep="\n")
            print()
            print( zip( string.ascii_uppercase, [ int(s) for s in sor.split()]) )
            print( *zip( string.ascii_uppercase, [ int(s) for s in sor.split()]) )
            print()
            print( dict( zip( string.ascii_uppercase, [ int(s) for s in sor.split()]) ))
            print("---\n")
            #'''

            continue

        adószám, utcanév, hsz, sáv, terület= sor.split()
        # Csak a területet konvertáljuk int-té, a többi karakterláncként is megfelel:
        t= int(terület)
        lutca.append( (adószám, utcanév, hsz, sáv, t) )

        ingatlan_adó= adó(sáv,t)

        # 5. feladat
        if sáv not in sum_adósáv:
            sum_adósáv[ sáv]= [0,0]

        sum_adósáv[ sáv][0] += 1
        sum_adósáv[ sáv][1] += ingatlan_adó

        # 6. feladat
        if utcanév not in utca_sávok:
            utca_sávok[ utcanév]= set()

        utca_sávok[ utcanév].add( sáv)

        # 7. feladat
        if adószám not in tulaj:
            tulaj[ adószám]= 0

        tulaj[ adószám] += ingatlan_adó


#--- 2. feladat
print( f"2. feladat. A mintában {len(lutca)} telek szerepel.")

#--- 3. feladat
bekért_adószám= input( "3. feladat. Egy tulajdonos adószáma: ").strip()

találat= 0
for adószám, utcanév, hsz, sáv, t in lutca:

    if adószám == bekért_adószám:
        print( f"{utcanév} utca {hsz}")
        találat += 1

if találat == 0:
    print( "Nem szerepel az adatállományban.")


#--- 5. feladat
print("5. feladat")

for sáv in sorted( adósávok.keys()):
    print( f"{sáv} sávba { sum_adósáv[ sáv][0] } telek esik, az adó {sum_adósáv[ sáv][1]:_} Ft.")


#--- 6. feladat
print( "6. feladat. A több sávba sorolt utcák:")

for utcanév in utca_sávok:
    if( len(utca_sávok[ utcanév])) > 1:
           print(utcanév)


#--- 7.feladat
with open( fn_fizetendő, "w") as fout:

    for adószám in tulaj:
        total= tulaj[ adószám]
        fout.write( f"{adószám} {total}\n")


#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben
