#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Utasszallitok.py
# Szakmai érettségi feladat: 2023. május, Utasszállítók, CLI
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2023

""" A feladatot a kiírás szerint Java vagy C# nyelven kellett megoldani,
    de mi most gyakorlásképpen Pythonban készítjük el.
"""

class Sebességkategória:

    kategóriák= ("Alacsony sebességű", "Szubszonikus", "Transzszonikus", "Szuperszonikus")

    def __init__( self, utazósebesség):

        self.__Utazósebesség= speed= int( utazósebesség)

        if speed < 500:
            self.__Kategórianév= self.kategóriák[0]
        elif speed < 1000:
            self.__Kategórianév= self.kategóriák[1]
        elif speed < 1200:
            self.__Kategórianév= self.kategóriák[2]
        else:
            self.__Kategórianév= self.kategóriák[3]

    @property
    def Kategórianév(self):
        return self.__Kategórianév


class Típus:

    def __init__( self, leírás):
        """
        típus;év;utas;személyzet;utazósebesség;felszállótömeg;fesztáv
        Airbus A300;1972;220-336;3;911;142000;44,84
        """
        self.név, self.év, self.utasok, self.személyzet, self.sebesség, self.tömeg, self.fesztáv = leírás.split(";")
        self.sebKat= Sebességkategória( self.sebesség)

        # "n1-n2".partition('-') --> [ "n1", "-", "n2"]
        # "n1".partition('-') --> ["n1","",""]
        minu, sep, maxu = self.utasok.partition("-")
        self.minUtas= int( minu)
        self.maxUtas= int( maxu) if sep else self.minUtas

        minsz, sep, maxsz =  self.személyzet.partition("-")
        self.minSzemélyzet= int( minsz)
        self.maxSzemélyzet= int( maxsz) if sep else self.minSzemélyzet

        self.fesztáv= float( self.fesztáv.replace( ",",".") )
        self.tömeg= int( self.tömeg )



class Gépek:

    def __init__( self, fn_input):

        self.típusok= []
        self.nBoeing= 0
        self.TMU= None              # a legtöbb utast szállító típus
        self.kategóriák= set()      # sebesség szerint

        with open( fn_input) as ff:

            next(ff)        # átugorjuk az első sort
            for sor in ff:

                sor= sor.strip()
                if not sor:
                    continue

                típus= Típus( sor)
                self.típusok.append( típus)

                if "Boeing" in típus.név:
                    self.nBoeing += 1

                if self.TMU:
                    if típus.maxUtas > self.TMU.maxUtas:
                        self.TMU= típus
                else:
                    self.TMU= típus

                self.kategóriák.add( típus.sebKat.Kategórianév)


    def feladat_4( self):
        print("\n4. feladat: Adatsorok száma:", len(self.típusok))


    def feladat_5( self):
        print("\n5. feladat: Boing típusok száma:", self.nBoeing)


    def feladat_6( self):
        print("\n6. feladat: A legtöbb utast szállító repülőgéptípus")
        print("\tTípus:", self.TMU.név)
        print("\tElső felszállás:", self.TMU.év)
        print("\tUtasok száma:", self.TMU.utasok)
        print("\tSzemélyzet:", self.TMU.személyzet)
        print("\tUtazó sebesség:", self.TMU.sebesség)


    def feladat_7( self):

        print("\n7. feladat:")
        sk= set( Sebességkategória.kategóriák) - self.kategóriák
        if not sk:
            print( "\tMinden sebességkategóriából van repülőgéptípus.")
        else:
            print( "\t", *sk, sep=" ")


    def feladat_8( self, fn_output):

        with open(fn_output, "w") as ff:

            ff.write( "típus;év;utas;személyzet;utazósebesség;felszállótömeg;fesztáv\n")
            for gép in self.típusok:

                ff.write( f"{gép.név};{gép.év};{gép.maxUtas};{gép.maxSzemélyzet};{gép.sebesség};{round(gép.tömeg/1000)};{round(gép.fesztáv*3.2808)}\n")


#---
if __name__ == "__main__":

    db= Gépek( "utasszallitok.txt")
    #db.dump()
    db.feladat_4()
    db.feladat_5()
    db.feladat_6()
    db.feladat_7()
    db.feladat_8( "utasszallitok_new.txt")

#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben

