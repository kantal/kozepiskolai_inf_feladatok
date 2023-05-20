#!/bin/env python3
# -*- coding: utf-8 -*-
# ellenorzo.py
# Érettségi feladat - digitális kultúra, középszint: 2023. május, TAJ-szám
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2023

def ellenőrzés( s_szám):

    összeg= 0
    s8= s_szám[:-1]     # s_szám[0:8]

    for sorszám, digit in enumerate( s8, 1):

        if sorszám % 2:
            összeg += 3*int(digit)
        else:
            összeg += 7*int(digit)

    if int(s_szám[-1]) == összeg % 10:
        return (True, összeg)
    return (False, összeg)


taj= input( "Kérem a TAJ-számot: ").strip()
#taj= "673457015"
#taj= "012345672"
print( "Az ellenőrzőszámjegy:", taj[-1] )

eredmény, summa= ellenőrzés( taj)
print( "A szorzatok összege:", summa)
print( "Helyes a szám!" if eredmény else "Hibás a szám!" )

#---------------------------------------------------------------------------
# További feladatok: https://github.com/kantal/kozepiskolai_inf_feladatok
# Ajánlott könyv:    Koós Antal: Python a gépben