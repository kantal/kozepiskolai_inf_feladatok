#!/usr/bin/env python3
# rgb.py
# Érettségi feladat - emelt szint: 2023. május, RGB-színek
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2023

class Kép:

    def __init__( self, fn_kép):

        with open( fn_kép) as ff:
            self.képsorok= [ [ int(v) for v in sor.strip().split() ] for sor in ff ]

        # A kép mérete pixelben:
        self.n_sor=  len( self.képsorok )
        self.n_oszlop= len( self.képsorok[0] ) // 3


    def pixel( self, sor, oszlop):
        """
        sor, oszlop: pixel koordináták, 1-től számítódnak
        Return: (red,green,blue)
        """
        index= 3*(oszlop-1)
        return tuple( self.képsorok[ sor-1][ index:index+3 ] )


    def feladat_2( self):

        print( "2. feladat:\nKérem egy képpont adatait!")
        sor= int( input("Sor: "))
        oszlop= int( input( "Oszlop: "))

        print( f"A képpont színe RGB{self.pixel( sor, oszlop)}")


    def feladat_3( self):

        print( "3. feladat:")
        n_vkp= 0     # világos pixelek száma
        self.legsötétebb_érték= 3*255

        for sor in range( 1, self.n_sor+1):
            for oszlop in range( 1, self.n_oszlop+1):

                summa= sum( self.pixel( sor, oszlop))
                if summa > 600:
                    n_vkp += 1
                if summa < self.legsötétebb_érték:   # 4. feladat
                    self.legsötétebb_érték= summa

        print( "A világos képpontok száma:", n_vkp )


    def feladat_4( self):

        print( "4. feladat:")
        print( "A legsötétebb pont RGB összege:", self.legsötétebb_érték)
        print( "A legsötétebb pixelek színe:" )

        for sor in range( 1, self.n_sor+1):
            for oszlop in range( 1, self.n_oszlop+1):

                pix= self.pixel( sor, oszlop)
                if sum(pix) == self.legsötétebb_érték:
                    print( f"RGB{pix}")


    def határ( self, sor, limit):
        # 5. feladat

        for oszlop in range( 2, self.n_oszlop+1):

            if abs( self.pixel( sor, oszlop)[2] - self.pixel( sor, oszlop-1)[2]) > limit:
                return True

        return False


    def feladat_6( self):
        print( "6. feladat:")

        for sor in range( 1, self.n_sor+1):
            if self.határ( sor, 10):
                print( "A felhő legfelső sora:", sor)
                break

        for sor in range( self.n_sor, 0 , -1):
            if self.határ( sor, 10):
                print( "A felhő legalsó sora:", sor)
                break

    """
    def feladat_6b( self):
        print( "6. feladat:")

        limes= [ sor for sor in range( 1, self.n_sor+1)  if self.határ( sor, 10) ]
        print( "A felhő legfelső sora:", limes[0])
        print( "A felhő legalsó sora:",  limes[-1])
    """


#---
if __name__ == "__main__":

    pic= Kép( "kep.txt")
    pic.feladat_2()
    pic.feladat_3()
    pic.feladat_4()
    pic.feladat_6()
    #pic.feladat_6b()

#---------------------------------------------------------------------------
# További feladatok: https://github.com/kantal/kozepiskolai_inf_feladatok
# Ajánlott könyv:    Koós Antal: Python a gépben

