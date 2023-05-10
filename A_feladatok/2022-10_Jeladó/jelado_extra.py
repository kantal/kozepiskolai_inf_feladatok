#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# jelado_extra.py
# Érettségi feladat: 2022. október, Jeladó
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2023

import math     # math.sqrt


class JelAdó:

    def __init__( self, fn_jel):

        self.jelek= []
        # A feladat szerint a koordináták a -10_000 és +10_000 közé esnek:
        self.x1 = self.y1 = 10_000
        self.x2 = self.y2 = -10_000

        self.elmozdulás= 0
        self.kimaradtak= []

        #--- 1. feladat
        with open( fn_jel) as ff:

            for sor in ff:

                sor= sor.strip()
                if not sor:
                    continue

                bejegyzés= [ int(v) for v in sor.split() ]
                óra, perc, mp, x, y = bejegyzés

                # 5. feladat
                if x < self.x1:
                    self.x1= x
                if x > self.x2:
                    self.x2= x
                if y < self.y1:
                    self.y1= y
                if y > self.y2:
                    self.y2= y

                # 6-7. feladat
                if len( self.jelek) > 1:

                    self.elmozdulás += math.sqrt( ( self.jelek[-2][3] - x ) ** 2 + ( self.jelek[-2][4] - y ) ** 2 )

                    dx= abs( x - self.jelek[-1][3] )
                    dy= abs( y - self.jelek[-1][4] )
                    dt= self.eltelt( bejegyzés, self.jelek[-1])

                    ndxy= ( max( dx,dy) -1 ) // 10
                    ndt= ( dt -1) // 300            # 5 perc == 300 mp

                    if ndxy > 0 or ndt > 0 :

                        if( ndt > ndxy):
                            self.kimaradtak.append( f"{óra} {perc} {mp} időeltérés {ndt}")
                        else:
                            self.kimaradtak.append( f"{óra} {perc} {mp} koordináta-eltérés {ndxy}")

                self.jelek.append( bejegyzés)



    def mutasd( self):
        print( *self.jelek, sep="\n")     # szemrevételezés


    def feladat_2( self):

        print("\n2. feladat")
        sorszám= int( input( "Adja meg a jel sorszámát! ") ) - 1
        print( f"x={ self.jelek[sorszám][3]} y={ self.jelek[sorszám][4]}")


    def eltelt( self, t1, t2):
        """
        --- 3. feladat
        t1 és t2 olyan legalább háromelemű indexelhető objektum,
        amelynek első elemei az óra, perc, mp értékek.
        """
        dtime= t1[0]*3600 + t1[1] * 60 + t1[2]  - t2[0]*3600 - t2[1] * 60 - t2[2]
        return dtime if dtime >= 0 else -dtime


    def feladat_4( self):

        ttime= self.eltelt( self.jelek[0][:4], self.jelek[-1][:4] )
        print( f"\n4. feladat\nIdőtartam: {ttime//3600}:{ttime%3600//60}:{ttime%60}" )


    def feladat_5( self):
        print( f"\n5. feladat\nBal alsó: {self.x1} {self.y1}, jobb felső: {self.x2} {self.y2}")


    def feladat_6( self):
        print( f"\n6. feladat\nElmozdulás: {self.elmozdulás:.3f} egység")


    def feladat_7( self, fn_kimaradt):

        with open( fn_kimaradt, "w") as ff:

            ff.write( "\n".join( self.kimaradtak) )


#---

if __name__ == "__main__":

    JA= JelAdó( "jel.txt")
    JA.feladat_2()
    JA.feladat_4()
    JA.feladat_5()
    JA.feladat_6()
    JA.feladat_7( "kimaradt.txt")


#---------------------------------------------------------------------------
# További feladatok: https://github.com/kantal/kozepiskolai_inf_feladatok
# Ajánlott könyv:    Koós Antal: Python a gépben
