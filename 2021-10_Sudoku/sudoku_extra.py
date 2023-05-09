#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# sudoku_extra.py
# Érettségi feladat: 2021. október, Sudoku
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2022

class Sudoku:


    def __init__( self, fsudoku= None):

        self.tábla= []
        self.lépések= []

        self.rt_nOszlop, self.rt_nSor= 3, 3   # egy résztábla mérete
        self.rt_perSor= 3   # a résztáblák száma egy sorban

        print( "1. feladat")

        if not fsudoku:
            self.fájlt_bekér()
        else:
            self.fsudoku= fsudoku
            print( "Fájl:", fsudoku)

        self.pozíciót_bekér()
        self.beolvas()


    def fájlt_bekér( self):
        self.fsudoku= input( "Adja meg a bemeneti fájl nevét! ").strip()


    def pozíciót_bekér( self):

        self.sor_bekért= int( input( "Adja meg egy sor számát! (1-9) ")) -1         # Az index 0-tól számítandó!
        self.oszlop_bekért= int( input( "Adja meg egy oszlop számát! (1-9) ")) -1


    def beolvas( self):

        # 2. feladat
        with open( self.fsudoku) as ff:

            sorszám= 0
            for sor in ff:

                sor= sor.strip()
                if not sor:
                    continue

                sorszám += 1
                sor= [ int(sz) for sz in sor.split() ]
                if sorszám <= 9:
                    self.tábla.append( sor)
                else:
                    self.lépések.append( sor)


    def feladat_3( self):

        # 3. feladat
        print( "\n3. feladat")

        szám= self.tábla[ self.sor_bekért][ self.oszlop_bekért]
        if szám != 0:
            print( f"Az adott helyen szereplő szám: {szám}")
        else:
            print( "Az adott helyet még nem töltötték ki.")

        print( f"A hely a(z) { self.résztábla_sorszáma() + 1 }. résztáblázathoz tartozik.")


    def résztábla_sorszáma( self, sor= None, oszlop= None):

        """ A megadja, hogy a megdott sor-oszlop pozíció melyik résztáblába esik.

        sor: int, 0-tól indul, sorpozíció a nagy táblában
        oszlop: int, 0-tól indul, oszloppozíció a nagy táblában

        Return: int, a bennfoglaló résztábla sorszáma, 0-tól indul
        """
        if sor == None:
            sor= self.sor_bekért
        if oszlop == None:
            oszlop= self.oszlop_bekért

        # a résztábla koordinátái
        rt_oszlop= oszlop // self.rt_nOszlop
        rt_sor=    sor // self.rt_nSor

        return  rt_sor * self.rt_perSor +  rt_oszlop


    def feladat_4( self):

        print( "\n4. feladat")
        arány= 100 * sum( s.count(0) for s in self.tábla) / 81
        print( f"Az üres helyek aránya: {arány:.1f}%" )


    def ellenőrzés( self, lépés):
        """
        lépés: pl. [9,1,2]  a szám, a sor és az  oszlop, ahol az utóbbi kettő
            1-től számítódik.
        Return: True/False, a lépés elvégezhető igen/nem
        """

        szám, sor, oszlop = lépés
        print( f"A kiválasztott sor: {sor} oszlop: {oszlop} a szám: {szám}")

        sor= sor - 1  # az index 0-tól indul
        oszlop= oszlop - 1

        if self.tábla[sor][oszlop] != 0:
            print( "A helyet már kitöltötték.\n")
            return False

        if szám in self.tábla[sor]:
            print( "Az adott sorban már szerepel a szám.\n")
            return False

        if any( self.tábla[ i][ oszlop] == szám  for i in range(9) ):
            print( "Az adott oszlopban már szerepel a szám.\n")
            return False

        sk= (sor // self.rt_nSor) * self.rt_nSor           # A résztábla bal-felső (kezdő) elemének sorpozíciója
        ok= (oszlop // self.rt_nOszlop) * self.rt_nOszlop  # és oszloppozíciója.

        if any( self.tábla[ sk+s][ ok+o] == szám  for s in range(3) for o in range(3) ):
            print( "Az adott résztáblázatban már szerepel a szám.\n")
            return False

        print( "A lépés megtehető.\n")
        return True


    def feladat_5( self):

        print( "\n5. feladat")
        for nso in self.lépések:
            self.ellenőrzés( nso)


if __name__ == "__main__":

    S= Sudoku()
    #S= Sudoku( "konnyu.txt")
    S.feladat_3()
    S.feladat_4()
    S.feladat_5()

#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben
