#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# eletjatek.py
# ÁGAZATI érettségi feladat: 2021. október, Életjáték, CLI
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2022

""" A feladatot a kiírás szerint Java vagy C# nyelven kellett megoldani,
    de mi most gyakorlásképpen Pythonban készítjük el.
"""

import random as rnd
import time

class ÉletjátekSzimulátor:

    jelCell= "S"
    #jelCel= "1"
    jelÜres= " "
    #jelÜres= "0"
    jelFüggKeret= "|"
    #jelFüggKeret= "X"
    jelVízKeret= "-"
    #jelVízKeret= "X"

    def __init__( self, sorok, oszlopok, seed= None):

        self.__SorokSzáma= sorok
        self.__OszlopokSzáma= oszlopok

        if seed:
            rnd.seed( seed)

        self.__Mátrix= []

        for s in range(sorok):

            sor= rnd.choices( (0,1), k= oszlopok)
            sor.insert(0,0)
            sor.append(0)
            self.__Mátrix.append( sor)

        self.__Mátrix.insert( 0, (oszlopok + 2) * [0] )
        self.__Mátrix.append( (oszlopok + 2) * [0] )


    def __megjelenít( self):

        print( ( self.__OszlopokSzáma + 2) * self.jelVízKeret)

        for isor in range( 1, self.__SorokSzáma+1):

            ls= [ self.jelCell if self.__Mátrix[ isor][o] else self.jelÜres  for o in range( 1, self.__OszlopokSzáma+1) ]
            ls.insert( 0, self.jelFüggKeret)
            ls.append( self.jelFüggKeret)
            print( *ls, sep="")

        print( ( self.__OszlopokSzáma + 2) * self.jelVízKeret)


    def __KövetkezőÁllapot( self):

        m= [ sor[:] for sor in self.__Mátrix ]

        deltas= ( (-1,-1), (-1,0), (-1,1),  (0,-1), (0,1),  (1,-1), (1,0), (1,1) )

        for sor in range( 1, self.__SorokSzáma+1):

            for oszlop in range( 1, self.__OszlopokSzáma):

                szomszédok= sum( self.__Mátrix[ sor + ds ][ oszlop + do ]  for ds,do in deltas )

                if self.__Mátrix[ sor][ oszlop]:

                    if szomszédok > 3 or szomszédok < 2:
                        m[ sor][oszlop]= 0
                else:
                    if szomszédok == 3:
                        m[ sor][oszlop]= 1

        self.__Mátrix= m


    def Run( self):

        self.__megjelenít()
        self.__KövetkezőÁllapot()
        time.sleep( 0.5)


#---
if __name__ == "__main__":

    E= ÉletjátekSzimulátor(10,10)
    E.Run()

    try:
        input("Indítás Enter-rel, megállítás Ctrl-C-vel.")
        while True:
            E.Run()

    except KeyboardInterrupt:
        print( )

#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben
