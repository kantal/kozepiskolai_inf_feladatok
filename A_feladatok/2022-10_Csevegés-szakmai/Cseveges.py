#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# Cseveges.py
# Szakmai érettségi feladat: 2022. október, Csevegés, CLI
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2023

""" A feladatot a kiírás szerint Java vagy C# nyelven kellett megoldani,
    de mi most gyakorlásképpen Pythonban készítjük el.
"""

import datetime as dt

#--- 2. feladat
class Beszélgetés:

    def __init__( self, bejegyzés):
        """
        bejegyzés: str
            21.09.27-15:00:37;21.09.27-15:04:19;Marci;Krisztián
        """
        self.tform= "%y.%m.%d-%H:%M:%S"
        tkezd, tbef, név1, név2 = bejegyzés.split(";")
        self.tkezd= dt.datetime.strptime( tkezd.strip(), self.tform)
        self.tbef= dt.datetime.strptime( tbef.strip(), self.tform)
        self.név1= név1.strip()
        self.név2= név2.strip()


class CsevDB:

    def __init__( self, fn_csevegés, fn_tagok):

        self.Tagok= []
        with open(fn_tagok) as ff:

            for tag in ff:
                tag= tag.strip()
                if tag:
                    self.Tagok.append( tag)

        self.Tagok.sort()

        self.Csevegések= []
        with open(fn_csevegés) as ff:

            next(ff)    # átugorjuk az első sort
            """
            # vagy üres sorokra is felkészülvén, figyelembe véve, hogy BOM van a megadott fájl elején: '\ufeffKezdet;...'
            while True:
                sor= next(ff).upper()
                if "KEZDET" in sor:
                    break
            """

            for sor in ff:
               sor= sor.strip()
               if sor:
                   self.Csevegések.append( Beszélgetés( sor))


    def feladat_4( self):
        print( f"4. feladat: Tagok száma: {len(self.Tagok)}fő - Beszélgetések: {len(self.Csevegések)}db")


    def feladat_5( self):
        print( "5. feladat: A leghosszabb beszélgetés adatai")

        lhb = max( self.Csevegések, key= lambda besz: besz.tbef - besz.tkezd )
        print( "\tKezdeményező:", lhb.név1 )
        print( "\tFogadó:      ", lhb.név2 )
        print( "\tKezdete:     ", self.dt2str( lhb.tkezd) )
        print( "\tVége:        ", self.dt2str( lhb.tbef) )
        print(f"\tHossza:       {(lhb.tbef-lhb.tkezd).seconds}mp" )


    def dt2str( self, dtime):
        return dtime.strftime( "%y.%m.%d-%H:%M:%S")

    def sec2str( self, secs):
        return f"{secs//3600:02}:{secs%3600//60:02}:{secs%60:02}"


    def feladat_6( self):
        tag= input( "6. feladat: Adja meg egy tag nevét: ").strip().upper()
        secs= 0
        for chat in self.Csevegések:

            if tag == chat.név1.upper()  or  tag == chat.név2.upper():
                secs += (chat.tbef - chat.tkezd).total_seconds()

        print( "\tA beszélgetések összes ideje:", self.sec2str( int(secs)) )


    def feladat_7( self):

        csendesek= []
        for tag in self.Tagok:
            for besz in self.Csevegések:
                if besz.név1 == tag  or besz.név2 == tag:
                    break
            else:
                csendesek.append( tag)

        print("7. feladat: Nem beszélgettek senkivel", *csendesek, sep='\n\t')


    def feladat_8( self):

        max_szünet= ( 0, None, None)   #  (tartam, t1:datetime, t2:datetime)
        """
        s  |-----|
               |--------|
                            |---------------|
                               |---|
                                        |-------|
        """
        előző_bef= dt.datetime(2021,9,27, 15)   # 2021.09.27-15:00:00 a naplózás kezdete (s)
        for besz in self.Csevegések:

            szünet= int( (besz.tkezd - előző_bef).total_seconds() )
            if szünet > max_szünet[0]:
                max_szünet= ( szünet, előző_bef, besz.tkezd)

            if besz.tbef > előző_bef:
                előző_bef= besz.tbef

        szünet, tkezd, tbef = max_szünet
        print( "8. feladat: A leghosszabb csendes időszak 15h-tól")
        print( "\tKezdete: ", self.dt2str( tkezd) )
        print( "\tVége:    ", self.dt2str( tbef) )
        print( "\tHossza:  ", self.sec2str( szünet) )


#---
if __name__ == "__main__":

    db= CsevDB( "csevegesek.txt", "tagok.txt")
    db.feladat_4()
    db.feladat_5()
    db.feladat_6()
    db.feladat_7()
    db.feladat_8()


#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben