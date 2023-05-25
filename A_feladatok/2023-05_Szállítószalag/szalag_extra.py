#!/usr/bin/env python3
# szalag_extra.py
# Érettségi feladat - emelt szint: 2023. május, Szállítószalag
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2023

import sys  # sys.exc_info()


def tav( szalaghossz, indulashelye, erkezeshelye ):

    if erkezeshelye >= indulashelye:
        return erkezeshelye - indulashelye
    return szalaghossz - indulashelye + erkezeshelye


class Rekesz:

    def __init__( self, sor, szalaghossz):

        self.tIndulás, self.honnan, self.hová, self.tömeg = [ int(v) for v in sor.split() ]
        self.távolság= tav( szalaghossz, self.honnan, self.hová)


class Műszak:

    def __init__( self, fn_adatok):

        print( "Adatfájl: ", fn_adatok)

        self.Mozgások= []
        self.leghosszabbTáv= 0
        self.tömeg_0= 0      # A 0. pozíció előtt áthaladt tömegek összege.

        with open( fn_adatok) as ff:

            lno= 1
            while not (sor:=next(ff).strip()) or sor[0] == '#':
                lno += 1

            try:
                self.szalaghossz, self.időegység  = [ int(v) for v in sor.split() ]
            except ValueError as esemény:
                raise ValueError( f"* NEM MEGFELELŐ SZALAGPARAMÉTEREK[{lno}]: '{sor}'\n{esemény}")

            for sor in ff:

                lno += 1

                sor= sor.strip()
                if not sor or sor[0] == '#':
                    continue

                try:
                    rek= Rekesz( sor, self.szalaghossz)
                except ValueError as esemény:
                    raise ValueError( f"* NEM MEGFELELŐ REKESZLEÍRÁS[{lno}]: '{sor}'\n{esemény}")

                self.Mozgások.append( rek)

                if rek.távolság > self.leghosszabbTáv:
                    self.leghosszabbTáv= rek.távolság

                if rek.honnan > rek.hová and rek.honnan != self.szalaghossz and rek.hová != 0 :
                    self.tömeg_0 += rek.tömeg


    def feladat_2( self):

        print("\n2. feladat")
        sorszám= input( f"Adja meg, melyik adatsorra kíváncsi ({1}-{ len(self.Mozgások)}): " )
        if not sorszám.isdigit():
            raise ValueError( f"* HIBÁSAN MEGADOTT SORSZÁM: '{sorszám}'" )

        sorszám= int( sorszám)

        if not ( 1 <= sorszám <= len( self.Mozgások) ):
            raise ValueError( f"* TÚL NAGY/KICSI SORSZÁM!: '{sorszám}'" )

        rekesz= self.Mozgások[ sorszám - 1]
        print( "Honnan:",  rekesz.honnan, "Hova:", rekesz.hová )


    def feladat_4( self):

        print("\n4. feladat")

        lhbb= [ index for (index,rek) in enumerate(self.Mozgások,1) if rek.távolság == self.leghosszabbTáv ]

        print( "A legnagyobb távolság:", self.leghosszabbTáv)
        print( "A maximális távolságú szállítások sorszáma:", *lhbb )


    def feladat_5( self):

        print("\n5. feladat")
        print( "A kezdőpont előtt elhaladó rekeszek össztömege:", self.tömeg_0)


    def feladat_6( self):

        print( "\n6. feladat")
        időpont= int( input( "Adja meg a kívánt időpontot! "))

        mozgásban= [ index for (index,rek) in enumerate(self.Mozgások,1) if rek.tIndulás <= időpont < (rek.tIndulás + rek.távolság * self.időegység) ]

        print( "A szállított rekeszek halmaza:", *mozgásban if mozgásban else ("üres",) )


    def feladat_7( self, fn_tömeg):

        iptm= dict()     # össztömegek az indulási pozíciók szerint

        for (index,rek) in enumerate(self.Mozgások,1):
            iptm[ rek.honnan]= iptm.get( rek.honnan, 0) + rek.tömeg

        with open( fn_tömeg, "w") as ff:

            for poz, össztömeg in sorted( iptm.items()):
                ff.write( f"{poz} {össztömeg}\n")



if __name__ == "__main__":

    try:
        db= Műszak( "teszt-szallit.txt")
        #db= Műszak( "valami.txt")
    except ValueError as esemény:
        print( f"* NEM SIKERÜLT AZ ADATOK BEOLVASÁSA")
        print( esemény)
        exit(1)
    except:
        print("* VALAMI GOND VAN!\n", sys.exc_info())
        exit(2)

    db.feladat_2()
    db.feladat_4()
    db.feladat_5()
    db.feladat_6()
    db.feladat_7( "teszt-tomeg.txt")


#---------------------------------------------------------------------------
# További feladatok: https://github.com/kantal/kozepiskolai_inf_feladatok
# Ajánlott könyv:    Koós Antal: Python a gépben
