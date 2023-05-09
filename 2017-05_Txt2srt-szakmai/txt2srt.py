#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# txt2srt.py
# ÁGAZATI érettségi feladat: 2017. május, Txt2Srt
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2018

#--- 1.,2.,3. feladat ---
class IdőzítettFelirat:

    def __init__(self, időzítés,felirat):
        """ időzítés, felirat: karakterláncok """
        
        self.időzítés, self.felirat= időzítés,felirat
        self.hossz= len(self.felirat.split())
        
    #--- 6. feladat ---
    def SzavakSzáma(self):
        return self.hossz
        
    #--- 8. feladat ---
    #Időzítés: „00:01 - 00:03”
    #SRT időzítés: „00:00:01 --> 00:00:03”
    def SrtIdőzítés(self):

        kezdés,vég= self.időzítés.split("-")
        kp,kmp= kezdés.split(":")
        vp,vmp= vég.split(":")

        kp,vp= int(kp),int(vp)  # egésszé alakítjuk
        kó,kp= kp//60, kp%60
        vó,vp= vp//60, vp%60

        kmp=kmp.strip() # karakterlánc maradt, levágjuk az elejéről és a végéről a szóközöket
        vmp=vmp.strip()

        return "{:02d}:{:02d}:{} --> {:02d}:{:02d}:{}".format(kó,kp,kmp,vó,vp,vmp)
        

class Feliratok:
    """ Az összes időzített feliratot fogja tartalmazni. """
    #--- 4. feladat ---
    def __init__(self,fájl):
        """ fájl: ahonnan a feliratokat be kell olvasni """
        
        self.feliratok=[]
        with open(fájl) as ff:
            for index,sor in enumerate(ff):
                sor= sor.strip()
                if not index%2:
                    időzítés=sor
                else:
                    self.feliratok.append( IdőzítettFelirat(időzítés,sor) )
        
    #--- 7. feladat ---
    def leghosszabb(self):
        return max( self.feliratok, key=lambda flirt: flirt.SzavakSzáma() )

    def darab(self):
        return len(self.feliratok)

    def mentMintSrt(self,fájl):
        """ fájl: a kimeneti fájl neve """
        
        with open(fájl,"w") as ff:
            for index,tétel in enumerate(self.feliratok):
                ff.write("{}\n{}\n{}\n\n".format(index+1,tétel.SrtIdőzítés(),tétel.felirat))
                
            
#-------------------------------------------------
if __name__ == "__main__":
    
    #--- 4. feladat ---
    FilmFeliratok= Feliratok("feliratok.txt")
    
    #--- 5. feladat ---
    print(FilmFeliratok.darab())
    
    #--- 7. feladat ---
    leghIdőzFeli= FilmFeliratok.leghosszabb()
    print(leghIdőzFeli.felirat)
    #print("  hossz: ", leghIdőzFeli.SzavakSzáma() )

    #print("Teszt:")
    #utolsó= FilmFeliratok.feliratok[-1]
    #print(utolsó.időzítés, utolsó.felirat)
    #print(utolsó.SrtIdőzítés())
    
    #--- 9. feladat ---
    FilmFeliratok.mentMintSrt("feliratok.srt")


#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben

