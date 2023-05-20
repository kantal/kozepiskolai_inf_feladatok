#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Labirintus.py
# Szakmai érettségi feladat: 2023. május, Labirintus, CLI
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2023

""" A feladatot a kiírás szerint Java vagy C# nyelven kellett megoldani,
    de mi most gyakorlásképpen Pythonban készítjük el.
"""

class LabSim:

    def __init__(self, fn_lab):

        self.__fn_lab= fn_lab
        self.__Adatsorok=[]
        self.__Lab=[]

        self.__KijáratOszlopIndex= -1
        self.__KijáratSorIndex= -1
        self.__NincsMegoldás= True
        self.__KeresésKész= False

        self.__BeolvasAdatsorok( fn_lab)

        self.__OszlopokSzáma= len( self.__Adatsorok[0])
        self.__SorokSzáma= len( self.__Adatsorok)

        self.__FeltöltLab()
        self.__KijáratOszlopIndex= self.__OszlopokSzáma - 1
        self.__KijáratSorIndex= self.__SorokSzáma - 2


    @property
    def KijáratOszlopIndex(self):
        return self.__KijáratOszlopIndex
    @property
    def KijáratSorIndex(self):
        return self.__KijáratSorIndex
    @property
    def OszlopokSzáma(self):
        return self.__OszlopokSzáma
    @property
    def SorokSzáma(self):
        return self.__SorokSzáma
    @property
    def KeresésKész(self):
        return self.__KeresésKész

    @property
    def NincsMegoldás(self):
        return self.__NincsMegoldás


    def __BeolvasAdatsorok(self, fn_lab):

        with open(fn_lab) as ff:

            sor= next(ff).strip()  # csupa 'X'
            self.__Adatsorok.append( sor)
            ncol= len(sor)

            for sor in ff:

                sor= sor.rstrip().ljust( ncol)
                self.__Adatsorok.append( sor)

            if not self.__Adatsorok[-1].startswith("X"):
                del self.__Adatsorok[-1]        # egy esetleges fájl végi üres sor elhagyása


    def __FeltöltLab(self):
        self.__Lab= [ list(sor) for sor in self.__Adatsorok ]
        #print( *self.__Lab, sep="\n")


    def feladat_5(self):

        print( f"\n5. feladat: Labirintus adatai ('{self.__fn_lab}')")
        print( f"\tSorok száma: {self.__SorokSzáma}\n\tOszlopok száma: {self.__OszlopokSzáma}")
        print( f"\n\tKijárat indexe: sor:{self.__KijáratSorIndex} oszlop:{self.__KijáratOszlopIndex}")


    def Kiírlab(self):

        for sor in self.__Lab:
            print( "".join(sor))


    def feladat_6(self):

        print("\n6. feladat: A labirintus")
        self.Kiírlab()


    def Útkeresés(self, hook= None):

        Lab= self.__Lab
        KeresésKész= False
        NincsMegoldás= False
        r= 1
        c= 0

        if hook:    # 8. feladat
            hook()

        while not KeresésKész and not NincsMegoldás:

            Lab[r][c]= 'O'
            if Lab[r][c+1] == ' ' :
                c += 1
            elif Lab[r+1][c] == ' ' :
                r += 1
            else:
                Lab[r][c]= '-'
                if Lab[r][c-1] == 'O':
                    c -= 1
                else:
                    r -= 1

            KeresésKész= r == self.KijáratSorIndex and c == self.KijáratOszlopIndex

            if KeresésKész:
                Lab[r][c]= 'O'

            NincsMegoldás= r == 1 and c == 0

            if hook:
                hook()

        self.__KeresésKész= KeresésKész
        self.__NincsMegoldás= NincsMegoldás


    def feladat_8(self):

        print( "\n8. feladat")

        def hook():
            input("\nNyomjon Entert\n")
            self.Kiírlab()

        self.Útkeresés( hook)
        print( "Nincs megoldás!" if self.__NincsMegoldás else "Útvonal megtalálva!")


#---
if __name__ == "__main__":

    fn_lab= "Lab1.txt"
    #fn_lab= "Lab2.txt"

    lab= LabSim( fn_lab )
    lab.feladat_5()
    lab.feladat_6()
    lab.feladat_8()

#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben
