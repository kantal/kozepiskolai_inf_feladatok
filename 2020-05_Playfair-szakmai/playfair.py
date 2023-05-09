#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# playfair.py
# ÁGAZATI érettségi feladat: 2020. május, Playfair-négyzet, CLI
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2020

""" A feladatot a kiírás szerint Java vagy C# nyelven kellett megoldani,
    de mi most gyakorlásképpen Pythonban készítjük el.
"""

class PlayfairKódoló:

    def __init__(self, fkódtábla):

        with open(fkódtábla) as ff:

            self.skódtábla= ff.read().replace(" ","").replace("\t","").replace("\n","").upper()

        self.tméret= 5


    def SorIndex(self,kar): # Nem fogjuk használni

        index= self.skódtábla.find(kar)
        if index!=-1:
            index//= self.tméret
        return index


    def OszlopIndex(self,kar): # Nem fogjuk használni

        index= self.skódtábla.find(kar)
        if index!=-1:
            index%= self.tméret
        return index


    def Index(self,kar): # Ezt fogjuk alkalmazni

        index= self.skódtábla.find(kar)
        if index==-1:
            return False

        return index//self.tméret, index%self.tméret


    # 7. feladat
    def KódolBetűpár(self,kk):

        if len(kk)!=2:
            return "?"

        s1o1= self.Index(kk[0])
        s2o2= self.Index(kk[1])

        if not s1o1 or not s2o2:
            return "?"

        s1,o1= s1o1
        s2,o2= s2o2
        if s1==s2:
            o1= (o1+1) % self.tméret
            o2= (o2+1) % self.tméret

        elif o1==o2:
            s1= (s1+1) % self.tméret
            s2= (s2+1) % self.tméret

        else:
            o1,o2= o2,o1

        return self.skódtábla[s1*self.tméret + o1] + self.skódtábla[s2*self.tméret + o2]

if __name__ == "__main__":

    #--- 1-5. feladat ---
    pk= PlayfairKódoló("kulcstabla.txt")

    #--- 6. feladat ---
    kar= input("6. feladat - Kérek egy nagy betűt: ").strip()
    si,oi= pk.Index(kar)
    print(f"A karakter sorának indexe: {si}\nA karakter oszlopának indexe: {oi}")

    #--- 8. feladat ---
    kk= input("8. feladat - Kérek egy karakterpárt: ").strip()
    print("Kódolva:", pk.KódolBetűpár(kk))


#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben
