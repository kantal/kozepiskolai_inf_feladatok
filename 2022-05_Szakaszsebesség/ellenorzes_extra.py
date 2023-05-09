#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# ellenorzes_extra.py
# Érettségi feladat: 2022. május, Ellenőrzés
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2022

import datetime as dt

fn_meresek= "meresek.txt"


def sebesség( t1, t2):
    """ Kiszámolja az átlagsebességet a 10km-es szakaszon

    t1, t2: a belépési és kilépési időpontok, datetime
    Return: int
    """
    return  10*3600/(t2 - t1).total_seconds()


def bírság( seb):
    """ Megadja a büntetési díjat

    seb: km/h, int
    Return: Ft, int
    """

    if seb <= 90:
        return 0

    if 104 < seb <= 121:
        return 30_000

    elif 121 < seb <= 136:
        return 45_000

    elif 136 < seb <= 151:
        return 60_000

    elif seb > 151:
        return 200_000

#---

lmeresek= []        # 1. feladat: a beolvasott adatok listája, [ [rendszám, t1, t2, sebesség] ...]
vp9_áthaladt= 0     # 3. feladat: a 9 óra előtt a végponton áthaladtak száma
autó_max_seb= ( None, 0,0,0);     # 5. feladat: (rendszám, t1, t2, sebesség)
gyorshajtók= []                      # 6. feladat: a 90 km/h-nál gyorsabbak

most= dt.datetime.now()

with open( fn_meresek) as ff:

    for sor in ff:

        sor= sor.strip()
        if not sor:
            continue

        rsz, h1,m1,s1,ms1, h2,m2,s2,ms2= sor.split()

        t1= dt.datetime( most.year, most.month, most.day, int(h1), int(m1), int(s1), 1000 * int(ms1))
        t2= dt.datetime( most.year, most.month, most.day, int(h2) ,int(m2) , int(s2), 1000 * int(ms2))
        seb= sebesség( t1,t2)
        lmeresek.append( [rsz, t1, t2, seb] )

        # 3. feladat
        if int( h2) < 9:
            vp9_áthaladt += 1

        # 5. feladat
        if seb > autó_max_seb[3]:
            autó_max_seb= ( rsz, t1, t2, seb)

        # 6., 7. feladat
        if seb > 90:
            gyorshajtók.append( lmeresek[-1] )


#print( *lmeresek, sep="\n")    # szemrevételezés

#--- 2. feladat
print( f"\n2. feladat\nA mérés során {len(lmeresek)} jármű adatait rögzítették.")

#--- 3. feladat
print( f"\n3. feladat\n9 óra előtt {vp9_áthaladt} jármű haladt el a végponti mérőnél.")

#--- 4. feladat
print( "\n4. feladat")
h,m = input( "Adjon meg egy óra és perc értéket! ").split()
h= int(h)
m= int(m)

kp_áthaladt= 0
forgalom= 0

lehagyott= 0    # 5. feladat
rsz_max, t1_max, t2_max, seb_max = autó_max_seb     # 5. feladat

t1_kért= dt.datetime( most.year, most.month, most.day, h, m, 0)
t2_kért= dt.datetime( most.year, most.month, most.day, h, m, 59, 999_000)


for rsz, t1, t2, seb in lmeresek:

    if t1.hour == h and t1.minute == m:
        kp_áthaladt += 1

    if t1 <= t2_kért and t2 >= t1_kért:
        forgalom += 1

    # 5. feladat
    if t1 < t1_max and t2 > t2_max:
        lehagyott += 1


print( f"\ta. A kezdeti méréspontnál elhaladt járművek száma: {kp_áthaladt}")
print( f"\tb. A forgalomsűrűség: {forgalom/10}")

#---  5. feladat
print( "\n5. feladat\nA legnagyobb sebességgel haladó jármű")
print( f"\trendszáma: {autó_max_seb[0]}")
print( f"\tátlagsebessége: { int(autó_max_seb[3]) } km/h")
print( f"\táltal lehagyott járművek száma: {lehagyott}")


#---  6. feladat
print( f"\n6. feladat\nA járművek {100 * len(gyorshajtók) / len(lmeresek):.2f}%-a volt gyorshajtó.")

#---  7. feladat
with open( "buntetes.txt", "w") as ff:

    for rsz, t1, t2, seb in gyorshajtók:

        if seb > 104:
            ff.write( f"{rsz};{ int(seb)} km/h;{bírság( seb)} Ft\n")

print( "\n7. feladat\nA fájl elkészült.")


#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben, 2. kiadás

