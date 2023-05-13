#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# BukkMaraton2019.py
# Szakmai érettségi feladat: 2022. október, Hegyikerékpár, CLI
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2023

""" A feladatot a kiírás szerint Java vagy C# nyelven kellett megoldani,
    de mi most gyakorlásképpen Pythonban készítjük el.
"""

#--- 2. feladat

class Versenytav:

    def __init__( self, rajtszám):

        self._Rajtszám= rajtszám
        self._Távok= { "M": "Mini", "R": "Rövid", "K": "Közép", "H": "Hosszú", "E": "Pedelec" }

    def get( self):
        return self._Távok.get( self._Rajtszám[0], "Hibás rajtszám")


class Maraton:

    indulók_száma= 691

    def __init__( self, fn_adatok):
        """ 3. feladat
        Rajtszám;Kategória;Név;Egyesület;Idő
        M107;m3f;Ács Zoltán;;1:21:25
        M15;fn;Adámi Krisztina;ÁkosBike Team Aszód;1:14:46
        R38;m2f;Adamkó Gergely;;1:58:10
        """

        self.Adatok= []
        with open( fn_adatok) as ff:

            next(ff)    # átugorjuk az első sort
            for sor in ff:

                sor= sor.strip()
                if not sor:
                    continue

                self.Adatok.append( [ t.strip() for t in sor.split(";") ] )
                # A bejegyzést kiegészítjük a mp-ben megadott idővel:
                ub= self.Adatok[-1]
                ub.append( self.str2sec( ub[-1]) )


    def str2sec( self, sidő):
        óra, perc, mp = sidő.split(":")
        return int(óra)*3600 + int(perc)*60 + int(mp)

    def mutat( self):
        print( *self.Adatok, sep="\n")


    def feladat_4( self):
        print( f"4. feladat: Versenytávot nem teljesítők: {(1-len(self.Adatok)/self.indulók_száma)*100:.2f}%")


    def feladat_5( self):

        n= 0
        for rsz, kat, név, klub, sidő, mp in self.Adatok:

            if kat[-1] == "n"  and  Versenytav( rsz).get() == "Rövid":
                n += 1

        print( f"5. feladat: Női versenyzők száma a rövid távú versenyen: {n}fő")


    def feladat_6( self):
        print( "6. feladat:", end= " ")

        t6óra= 6*3600     # sec
        for bejegyzés in self.Adatok:

            if bejegyzés[-1] > t6óra:
                print( "Volt ilyen versenyző")
                #print( bejegyzés)
                return

        print( "Nem volt ilyen versenyző")


    def feladat_7( self):
        print( "7. feladat: A felnőtt férfi (ff) kategória győztese rövid távon")

        tsec= 86400  # a legjobb teljesítési idő
        idxbejegyzés= None
        for index, (rsz, kat, név, klub, sidő, mp) in enumerate( self.Adatok):

            if rsz[0] == "R" and kat == "ff" and mp < tsec:

                tsec= mp
                idxbejegyzés= index

        if idxbejegyzés:

            rsz, kat, név, klub, sidő, mp = self.Adatok[ idxbejegyzés]
            print( "\tRajtszám: ", rsz )
            print( "\tNév:      ", név )
            print( "\tEgyesület:", klub)
            print( "\tIdő:      ", sidő)


    def feladat_8( self):
        print( "8. feladat: Statisztika")

        stat= dict()
        for bejegy in self.Adatok:

            kat= bejegy[1]
            if kat[-1] == "f":
                stat[ kat ]= stat.get( kat, 0) + 1

        for kat, fő in stat.items():
            print( f"\t{kat} - {fő}fő")


#---
if __name__ == "__main__":

    db= Maraton( "bukkm2019.txt");
    #db.mutat()
    db.feladat_4()
    db.feladat_5()
    db.feladat_6()
    db.feladat_7()
    db.feladat_8()



#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben