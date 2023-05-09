#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# ADFGVX.py
# ÁGAZATI érettségi feladat: 2020. október, ADFGVX-rejtjelezés, CLI
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2020

""" A feladatot a kiírás szerint Java vagy C# nyelven kellett megoldani,
    de mi most gyakorlásképpen Pythonban készítjük el.
"""

# adfgvx_txt.py a csharp.txt átirata Pythonra:
from adfgvx_txt import ADFGVXrejtjel


def Beker(defkulcs= "HOLD", defuzenet= "szeretem a csokit"):

    print("2. feladat:")
    kulcs= input(f"\tKérem a kulcsot [{defkulcs}]:").strip().upper()
    uzenet= input(f"\tKérem az üzenetet [{defuzenet}]:").strip().lower()
    if not kulcs:
        kulcs= defkulcs
    if not uzenet:
        uzenet= defuzenet

    return uzenet,kulcs

#--
# Új osztályt hozunk létre a korábbiból
class Rejt(ADFGVXrejtjel):

    def AtalakitottUzenet(self):

        uzenet= self.Uzenet.replace(" ","")
        maradek= len(uzenet) % len(self.Kulcs)
        if maradek:
            uzenet+= (len(self.Kulcs)-maradek) * "x"

        return uzenet

    """
    Függvény Betupar(k: karakter): sztring
        Változó adfgvx[0..5]: sztring elemű tömb {”A”,”D”,”F”,”G”,”V”,”X”}
        Ciklus sorIndex:=0-tól 5-ig egyesével
            Ciklus oszlopIndex:=0-tól 5-ig egyesével
                Ha Kodtabla[sorIndex, oszlopIndex] = k
                    térj vissza adfgvx[sorIndex] + adfgvx[oszlopIndex]
                Elágazás vége
            Ciklus vége
        Ciklus vége
        térj vissza ”hiba”
    Függvény vége
    """
    def Betupar(self,k):

        adfgvx= list("ADFGVX")

        for isor in range(6):
            for ioszlop in range(6):

                if self.Kodtabla[isor][ioszlop] == k:
                    return adfgvx[isor] + adfgvx[ioszlop]

        raise ValueError("Hiba a 'Betupar()' futása közben.")


    def Kodszoveg(self):

        atalakitott_uzenet= self.AtalakitottUzenet()
        s=""
        for k in atalakitott_uzenet:
            s+= self.Betupar(k)

        return s

#--------

def Feladat(R):
    print("5. feladat: Az átalakított üzenet:", R.AtalakitottUzenet())
    print(f"6. feladat: s->{R.Betupar('s')} x->{R.Betupar('x')}")
    print("7. feladat: A kódszöveg:", R.Kodszoveg())
    print("8. feladat: A kódolt üzenet:", R.KodoltUzenet())

#--
# példányosítás
R1= Rejt("kodtabla.txt", *Beker())
Feladat(R1)
print("---")

R2= Rejt("kodtabla.txt",*Beker())
#R2= Rejt("kodtabla.txt", "Az igazak orokke elnek","jedlik")
Feladat(R2)


#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben
