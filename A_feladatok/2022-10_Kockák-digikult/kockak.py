#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# kockak.py
# Érettségi feladat - digitális kultúra, középszint: 2022. október, Kockák
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2023

import random

N= int( input( "Hány alkalommal legyen feldobás? " ) )
oldalak= range(1,7)
nAnni= 0

for n in range(N):

    d1= random.choice( oldalak)
    d2= random.choice( oldalak)
    d3= random.choice( oldalak)
    összeg= d1 + d2 + d3

    if összeg < 10:
        lány= "Anni"
        nAnni += 1
    else:
        lány= "Panni"

    print( f"Dobás: {d1} + {d2} + {d3} = {összeg}\tNyert: {lány}" )


print( f"A játék során {nAnni} alkalommal Anni, {N-nAnni} alkalommal Panni nyert.")

#---------------------------------------------------------------------------
# További feladatok: https://github.com/kantal/kozepiskolai_inf_feladatok
# Ajánlott könyv:    Koós Antal: Python a gépben
