#!/bin/env python3
# -*- coding: utf-8 -*-
# kitalalo.py
# Érettségi feladat - digitális kultúra, középszint: 2023. május, Kitaláló
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2023

import random

szavak= [ "fuvola", "csirke", "adatok", "asztal", "fogoly", "bicska", "farkas", "almafa", "babona", "gerinc", "dervis", "bagoly", "ecetes", "angyal", "boglya" ]

szóhossz= 6
kiválasztott= random.choice( szavak)
#print( kiválasztott)

sválasz= "Az eredmény:   "
skérdés= "\nKérem a tippet: "
'''
skérdés= """
                123456
Kérem a tippet: """
'''

próbaszám= 0
while True:

    próbaszám += 1
    eredmény= ""

    tipp= input( skérdés).strip()

    if tipp == "stop":
        break

    if len(tipp) != szóhossz:
        print( f"Szóhossz {szóhossz}!")
        continue

    for i in range( szóhossz):
        if tipp[i] == kiválasztott[i]:
            eredmény += tipp[i]
        else:
            eredmény += "."

    print( sválasz, eredmény)

    if eredmény == kiválasztott:

        print( próbaszám, "tippeléssel sikerült kitalálni.")
        break

#---------------------------------------------------------------------------
# További feladatok: https://github.com/kantal/kozepiskolai_inf_feladatok
# Ajánlott könyv:    Koós Antal: Python a gépben
