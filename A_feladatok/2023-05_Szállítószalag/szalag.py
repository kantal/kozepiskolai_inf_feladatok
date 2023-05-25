#!/usr/bin/env python3
# szalag.py
# Érettségi feladat - emelt szint: 2023. május, Szállítószalag
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2023


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

        self.Mozgások= []
        self.leghosszabbTáv= 0
        self.tömeg_0= 0      # A 0. pozíció előtt áthaladt tömegek összege.

        with open( fn_adatok) as ff:

            self.szalaghossz, self.időegység  = [ int(v) for v in next(ff).split() ]

            for sor in ff:

                sor= sor.strip()
                if not sor:
                    continue

                rek= Rekesz( sor, self.szalaghossz)
                self.Mozgások.append( rek)

                if rek.távolság > self.leghosszabbTáv:
                    self.leghosszabbTáv= rek.távolság

                if rek.honnan > rek.hová and rek.honnan != self.szalaghossz and rek.hová != 0 :
                    self.tömeg_0 += rek.tömeg


    def feladat_2( self):

        print("\n2. feladat")
        sorszám= int( input( "Adja meg, melyik adatsorra kíváncsi! "))
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

        print( "A szállított rekeszek halmaza:", end=" ")
        if mozgásban:
              print( *mozgásban)
        else:
            print( "üres")


    def feladat_7( self, fn_tömeg):

        iptm= dict()     # össztömegek az indulási pozíciók szerint

        for (index,rek) in enumerate(self.Mozgások,1):
            iptm[ rek.honnan]= iptm.get( rek.honnan, 0) + rek.tömeg

        with open( fn_tömeg, "w") as ff:

            for poz, össztömeg in sorted( iptm.items()):
                ff.write( f"{poz} {össztömeg}\n")



if __name__ == "__main__":

    db= Műszak( "szallit.txt")
    db.feladat_2()
    db.feladat_4()
    db.feladat_5()
    db.feladat_6()
    db.feladat_7( "tomeg.txt")


#---------------------------------------------------------------------------
# További feladatok: https://github.com/kantal/kozepiskolai_inf_feladatok
# Ajánlott könyv:    Koós Antal: Python a gépben
