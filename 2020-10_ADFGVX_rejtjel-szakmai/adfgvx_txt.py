#!/usr/bin/env python3
#-*- coding:utf-8 -*-

# A csharp.txt átirata Pythonra

class ADFGVXrejtjel:

    def AtalakitottUzenet(self):
        # 5. feladat:
        return "teszt"

    def Kodszoveg(self):
        # 7. feladat:
        return "teszt"


    def KodoltUzenet(self):

        kodszoveg= self.Kodszoveg()
        sorokSzama= len(kodszoveg) // len(self.Kulcs)
        oszlopokSzama= len(self.Kulcs)
        m= [ [0 for i in range(oszlopokSzama)] for j in range(sorokSzama) ]

        index= 0
        for sor in range(sorokSzama):
            for oszlop in range(oszlopokSzama):
                m[sor][oszlop]= kodszoveg[index]
                index+=1

        kodoltUzenet= ""
        for ch in range(ord("A"),ord("Z")+1):

            ch= chr(ch)
            oszlopIndex = self.Kulcs.find(ch)
            if oszlopIndex != -1:

                for sorIndex in range(sorokSzama):
                    kodoltUzenet += m[sorIndex][oszlopIndex]

        return kodoltUzenet;


    def __init__(self,kodtablaFile,uzenet,kulcs):

        self.Uzenet, self.Kulcs= uzenet.strip().lower(), kulcs.strip().upper()

        with open(kodtablaFile) as ff:
            self.Kodtabla= ff.readlines()
