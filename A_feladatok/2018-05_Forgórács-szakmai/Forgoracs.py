#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# forgoracs.py
# ÁGAZATI érettségi feladat: 2018. május, Forgórács
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2018

#--- 1.,2.,3.,4. feladat ---
# A 'Titkosítandó' változónak csak olvashatónak kellene lennie, de a Pythonban erre, szándékosan,
# nincs nyelvi konstrukció. Lásd a külön privát.py kódot, amelyben mutatunk megoldást.
class Frács:
    
    def __init__(self, fkódlemez, szöveg):
        
        self.Titkosított= [ ["."]*8 for n in range(8) ]
        self.Titkosítandó= szöveg  
        self.Átalakít()
        
        with open(fkódlemez) as ff:
            self.Kódlemez= [ list(sor.strip()) for sor in ff ]

            
    def Átalakít(self):
        
        self.Titkosítandó= self.Titkosítandó.replace(" ","").replace(".","").replace(",","")
        if len(self.Titkosítandó) > 64:
            raise ValueError("Túl hosszú a titkosítandó szöveg!")
        self.Titkosítandó= "{:X<64}".format(self.Titkosítandó)
        
    #--- 7.,10. feladat ---
    def PrintMátrix(self,mátrix):
        for sor in mátrix:
            print("".join(sor))
        print()
        
    #--- 7. feladat ---
    def KiírKódlemez(self):
        self.PrintMátrix(self.Kódlemez)
        
    #--- 9. feladat ---                    
    """
    Függvény ForgatKodlemez(): Karakter típusú mátrix
        Változó ujKodlemez: Karakter típusú 8x8-as mátrix
        Ciklus sor:=0-tól 7-ig egyesével
            Ciklus oszlop:=0-tól 7-ig egyesével
                ujKodlemez[7-oszlop, sor] = Kodlemez[sor, oszlop]
            Ciklus vége
        Ciklus vége
        Térj vissza ujKodlemez
    """
    def ForgatKódlemez(self):

        újKódlemez= [ ['']*8 for n in range(8) ]
        for sor in range(8):
            for oszlop in range(8):
                újKódlemez[7-oszlop][sor]= self.Kódlemez[sor][oszlop]
        return újKódlemez

    #--- 10. feladat ---                    
    def Titikosít(self):
        
        karindex=0
        for menet in range(4):
            for oszlop in range(8):     # Az oszlopokon megyünk "lefelé".
                for sor in range(8):
                    if  self.Kódlemez[sor][oszlop]=="A":
                        self.Titkosított[sor][oszlop]= self.Titkosítandó[karindex]
                        karindex+=1
            # Egyszer végignéztük a mátrixot, és tudjuk, hogy egy menetben pontosan 16 'A'-t
            # találunk; tehát forgatunk:
            self.Kódlemez=self.ForgatKódlemez() 

                            
#--- 5. feladat ---                    
print("\n5. feladat:")

with open("szoveg.txt") as ff:
    szöveg= ff.read().strip()
print(szöveg)

#--- 6. feladat ---                    
obrács= Frács("kodlemez.txt",szöveg)

#--- 7. feladat ---                    
print("\n7. feladat:")
obrács.KiírKódlemez()

#--- 8. feladat ---                    
print("\n8. feladat:")
print(obrács.Titkosítandó)

#--- 10. feladat ---                    
print("\n10. feladat:")
obrács.Titikosít()
obrács.PrintMátrix(obrács.Titkosított)


#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben

