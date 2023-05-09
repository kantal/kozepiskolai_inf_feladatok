#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# KarakterDekodolo.py
# ÁGAZATI érettségi feladat: 2022. május, Karakterdekódoló, CLI
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2022

""" A feladatot a kiírás szerint Java vagy C# nyelven kellett megoldani,
    de mi most gyakorlásképpen Pythonban készítjük el.
"""

import string

#--- 2. feladat
class Karakter:

    def __init__(self, betű, mátrix= None):
        """
        betű: angol nagy betű, str, pl. "A"
        mátrix: a bitkép sorainak listája
        """

        self.betű= betű
        self.mátrix= mátrix if mátrix else []

    def __str__( self):
        return f"{self.betű}\n" + "\n".join( self.mátrix)


    def Felismer( self, másik):
        return self.mátrix == másik.mátrix


class KarakterBank:

    def __init__( self, bank_file):

        self.Bank= []       # az adatok betöltéséhez
        self.DiBank= dict() # a kereséshez/kódoláshoz

        with open( bank_file) as ff:

            for sor in ff:

                sor= sor.strip()
                if not sor:
                    continue

                if len( sor) == 1:

                    if sor in self.DiBank:  # kiegészítés a 8. feladat miatt, egyedi kulcsok készítése
                        sor= sor + str( len( self.DiBank))

                    K= Karakter( sor)
                    self.Bank.append( K)
                    self.DiBank[ sor]= K
                else:
                    self.Bank[ -1].mátrix.append( sor)

    def __len__( self):
        return len( self.Bank)


    def __contains__( self, betű):
        return True if betű in self.DiBank else False


if __name__ == "__main__":

    #--- 4. feladat
    f_bank= "bank.txt"
    KB= KarakterBank( f_bank)
    print( *KB.DiBank.values(), sep="\n\n")   # szemrevételezés

    #--- 5. feladat
    print( f"5. feladat: Karakterek száma: {len(KB)}")

    #--- 6. feladat
    while True:

        betű= input("6. feladat: Kérek egy angol nagy betűt: ").strip()
        if len(betű) == 1  and  betű in string.ascii_uppercase:
            break

    #--- 7. feladat
    print("7. feladat")

    if betű not in KB:
        print("Nincs ilyen karakter a bankban!")
    else:
        print( str(KB.DiBank[ betű]).replace("0"," ").replace("1","X") )


    #--- 8. feladat
    f_szó= "dekodol.txt"
    Szó= KarakterBank( f_szó)

    #print("\nSzó:")   # szemrevételezés
    #print( *Szó.DiBank.values(), sep="\n\n")


    #--- 9. feladat
    print( "9. feladat: Dekódolás")

    megfejtés= []
    for k_ismeretlen in Szó.Bank:
        for kar in KB.Bank:

            if kar.Felismer( k_ismeretlen):
                megfejtés.append( kar.betű)
                break
        else:
            megfejtés.append( "?")

    print( "".join(megfejtés) )


#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben
