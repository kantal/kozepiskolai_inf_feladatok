#!/bin/env python3
# -*- coding: utf-8 -*-
# ellenorzo_extra.py
# Érettségi feladat - digitális kultúra, középszint: 2023. május, TAJ-szám
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2023

def ellenőrzés( s_szám):

    if len(s_szám) != 9:
        return False, 0, "* HIBA: Érvénytelen a TAJ szám mérete!"

    if not s_szám.isdigit():
        return False, 0, "* HIBA: Nem csak számokat tartalmaz!"

    összeg= sum( int(d)*sz for d,sz in zip( s_szám, [3,7,3,7,3,7,3,7]) )

    return (True, összeg, "Helyes a szám!" ) if int(s_szám[-1]) == összeg % 10  else (False, összeg, "* Hibás a szám!")



if __name__ == "__main__":

    tajlista= [ " ", "673457015", "012345672" ]

    bekért= input( "Kérem a TAJ-számot: ").strip()
    if bekért:
        tajlista= [ bekért]

    for taj in tajlista:

        print( f"\nTAJ: '{taj}'\nAz ellenőrzőszámjegy: {taj[-1]}" )

        eredmény, summa, magyarázat= ellenőrzés( taj)
        print( "A szorzatok összege:", summa)
        print( magyarázat)

#---------------------------------------------------------------------------
# További feladatok: https://github.com/kantal/kozepiskolai_inf_feladatok
# Ajánlott könyv:    Koós Antal: Python a gépben
