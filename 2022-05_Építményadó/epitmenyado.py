#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# epitmenyado.py
# Érettségi feladat: 2022. május, Építményadó
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2022


fn_utca= "utca.txt"
fn_fizetendő= "fizetendo.txt"

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


#--- 1. feladat
""" Az 'lutca' listában tároljuk az utca.txt adatait, plusz
az ingatlanonként fizetendő adót. Feltöltjük az 'adósávok' dict-et is.
"""
lutca= []
with  open( fn_utca) as ff:

    for sor in ff:

        sor= sor.strip()
        if not sor:
            continue    # az esetleges üres sorokat átugorjuk

        if not adósávok:
            # még az 'adósávok' dict üres, ebből a(z első) sorból töltjük fel
            n1,n2,n3= sor.split()
            adósávok['A']= int(n1)
            adósávok['B']= int(n2)
            adósávok['C']= int(n3)
            continue

        adószám, utcanév, hsz, sáv, terület= sor.split()
        # Csak a területet konvertáljuk int-té, a többi karakterláncként is megfelel:
        t= int(terület)
        lutca.append( (adószám, utcanév, hsz, sáv, t, adó(sáv,t)) )

#print( *lutca, sep="\n")    # szemrevételezés

#--- 2. feladat
print( f"2. feladat. A mintában {len(lutca)} telek szerepel.")


#--- 3. feladat
bekért_adószám= input( "3. feladat. Egy tulajdonos adószáma: ").strip()

találat= 0
for adószám, utcanév, hsz, sáv, t, számított_adó in lutca:

    if adószám == bekért_adószám:
        print( f"{utcanév} utca {hsz}")
        találat += 1

if találat == 0:
    print( "Nem szerepel az adatállományban.")


#--- 5. feladat
print("5. feladat")

sum_adósáv= dict()  # pl. 'A' --> [ telkek száma, adóösszeg ]
for adószám, utcanév, hsz, sáv, t, számított_adó in lutca:

    if sáv not in sum_adósáv:
        sum_adósáv[ sáv]= [0,0]

    sum_adósáv[ sáv][0] += 1
    sum_adósáv[ sáv][1] += számított_adó

for sáv in "ABC":
    print( f"{sáv} sávba {sum_adósáv[ sáv][0]} telek esik, az adó {sum_adósáv[ sáv][1]} Ft.")


#--- 6. feladat
print( "6. feladat. A több sávba sorolt utcák:")

utca_sávok= dict()  # utcanév --> set( ) a sávok készlete
for adószám, utcanév, hsz, sáv, t, számított_adó in lutca:

    if utcanév not in utca_sávok:
        utca_sávok[ utcanév]= set()

    utca_sávok[ utcanév].add( sáv)

for utcanév in utca_sávok:

    if( len(utca_sávok[ utcanév])) > 1:
           print(utcanév)


#--- 7.feladat

tulaj= dict()   # adószám --> szumma adó
for adószám, utcanév, hsz, sáv, t, számított_adó in lutca:

    if adószám not in tulaj:
        tulaj[ adószám]= 0

    tulaj[ adószám] += számított_adó

with open( fn_fizetendő, "w") as fout:

    for adószám in tulaj:
        fout.write( f"{adószám} { tulaj[ adószám] }\n")


#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben
