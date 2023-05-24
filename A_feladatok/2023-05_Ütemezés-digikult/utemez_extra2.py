#!/usr/bin/env python3
# utemez_extra2.py
# Érettségi feladat - digitális kultúra, emelt szint: 2023. május, Ütemezés
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2023

import datetime as dt

class Tábor:

    def __init__( self, bejegyzés):

        self.hó1, self.nap1, self.hó2, self.nap2, self.nevek, self.téma = bejegyzés.strip().split()
        self.kezdete= dt.datetime( 2023, int(self.hó1), int(self.nap1) )
        self.vége= dt.datetime( 2023, int(self.hó2), int(self.nap2) )
        self.zenei= True if "zenei" in self.téma else False
        self.jelentkezőkSzáma= len( self.nevek)


class Táborok:

    def __init__( self, fn_adatok):

        self.táborok= []
        self.maxJelentkező= 0

        with open( fn_adatok) as ff:

            for sor in ff:

                sor= sor.strip()
                if not sor:
                    continue

                tábor= Tábor( sor)
                self.táborok.append( tábor)

                if tábor.jelentkezőkSzáma > self.maxJelentkező:
                    self.maxJelentkező= tábor.jelentkezőkSzáma


    def feladat_2( self):

        print( "\n2. feladat\nAz adatsorok száma:", len( self.táborok) )
        print( "Az először rögzített tábor témája:", self.táborok[0].téma )
        print( "Az utoljára rögzített tábor témája:",  self.táborok[-1].téma )


    def feladat_3( self):

        print( "\n3. feladat")
        van_zenei= False

        for t in self.táborok:
            if t.zenei:
                print( f"Zenei tábor kezdődik {t.hó1}. hó {t.nap1}. napján.")
                van_zenei= True

        if not van_zenei:
            print( "Nem volt zenei tábor.")


    def feladat_4( self):

        print( "\n4. feladat")
        print( "Legnépszerűbbek:")

        for t in self.táborok:

            if self.maxJelentkező == t.jelentkezőkSzáma:
                print( t.hó1, t.nap1, t.téma )


    def feladat_6( self):

        print( "\n6. feladat")
        időpont= dt.datetime( 2023, int(input( "hó: ")), int(input( "nap: ")) )

        táborok_száma= sum( 1 for t in self.táborok if t.kezdete <= időpont <= t.vége )
        print( f"Ekkor éppen {táborok_száma} tábor tart.")


    def feladat_7( self, fn_tanuló):

        print( "\n7. feladat")

        tanuló= input( "Adja meg egy tanuló betűjelét: ").strip().upper()

        camps= [ t for t in self.táborok if tanuló in t.nevek ]
        camps= sorted( camps, key= lambda t: t.kezdete )

        előzőVége= dt.datetime( 2023, 6, 15)    # A szünet előtti utolsó nap.
        átfedés= False
        with open( fn_tanuló, "w") as ff:

            for t in camps:

                if not átfedés:
                    if t.kezdete <= előzőVége:
                        átfedés= True
                    else:
                        előzőVége= t.vége

                ff.write( f"{t.hó1}.{t.nap1}-{t.hó2}.{t.nap2}. {t.téma}\n")

        if not átfedés:
            print( "Mindegyik táborba elmehet")
        else:
            print( "Nem mehet el mindegyik táborba.")


#--- 5. feladat
# Nem használjuk
def sorszám( hónap, nap):
    # jún. 16-tól aug. 31-ig
    hó_napjai= ( 30-16+1, 31, 31)
    if hónap == 6:
        return nap - 16 +1

    return sum( hó_napjai[ :hónap-6] ) + nap


#---
if __name__ == "__main__":

    db= Táborok( "taborok.txt")
    db.feladat_2()
    db.feladat_3()
    db.feladat_4()
    db.feladat_6()
    db.feladat_7( "egytanulo.txt")


#---------------------------------------------------------------------------
# További feladatok: https://github.com/kantal/kozepiskolai_inf_feladatok
# Ajánlott könyv:    Koós Antal: Python a gépben

