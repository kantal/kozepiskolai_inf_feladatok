#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# reversi_extra.py
# Érettségi feladat: 2017. október, Reversi
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2017

class Tabla:

    def __init__(self, fname):
        """ 1.,2.,3. feladat """
        self.t= []
        with open(fname) as ff:
            sor_száma=0         # a hibás sor számának megjelenítéséhez
            oszlopok= 0         # az oszlopok száma minden sorban azonos kell legyen
            for line in ff:
                sor_száma+=1
                line= list( line.strip().upper() )  # "K" és "k" egyaránt jó lesz
                if not line:
                    raise ValueError("Üres sor: {}. sor!".format(sor_száma))
                if not oszlopok:
                    oszlopok=len(line)
                if len(line)!=oszlopok:
                    raise ValueError("Eltérő sorhossz: {}. sor!".format(sor_száma))
                for kar in line:
                    if kar not in ("F","K","#"):    # más karektert nem fogadunk el
                        raise ValueError("Hibás karakter: {}. sor!".format(sor_száma))

                self.t.append(line)
        #print(self.t)    # teszt


    def Megjelenit(self):
        """ 5. feladat """
        for sor in self.t:
            print("\t"+"".join(sor))


    def Megszamlal(self,mit):
        """ 6. feladat """
        return sum( [sor.count(mit) for sor in self.t] )


    def VanForditas(self, jatekos, sor, oszlop, iranySor, iranyOszlop):
        """ 7. feladat """
        if self.t[sor][oszlop]!="#":
            return False

        aktSor= sor + iranySor
        aktOszlop= oszlop + iranyOszlop
        ellenfel= "K" if jatekos != "K" else "F"

        nincsEllenfel= True

        while 0<=aktSor<8 and  0<=aktOszlop<8 and self.t[aktSor][aktOszlop]==ellenfel:
            aktSor+= iranySor
            aktOszlop+= iranyOszlop
            nincsEllenfel= False

        if nincsEllenfel or aktSor<0 or aktSor>7 or aktOszlop<0 or aktOszlop>7 or self.t[aktSor][aktOszlop]!=jatekos:
            return False

        return True


    def inpVanForditas(self):
        """ Segédfgv a 7. feladathoz """
        j,s,o,irs,iro= input("[ jatekos;sor;oszlop;iranySor;iranyOszlop ] = ").split(";")
        j=j.strip().upper()     # F ; 4; 1; 0;1  <-- szóközök megengedve
        if j not in ("K","F"):
            raise ValueError("Hibás input!")

        return self.VanForditas(j,int(s),int(o),int(irs),int(iro))


    def Szabalyos(self,jatekos,sor,oszlop):
        """ 9. feladat """
        for iranySor,iranyOszlop in ( (-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1) ):

            if self.VanForditas(jatekos, sor, oszlop, iranySor, iranyOszlop):
                return True

        return False


    def inpSzabalyos(self):
        """ Segédfgv a 9. feladathoz """
        j,s,o= input("[ jatekos;sor;oszlop ] = ").split(";")
        j=j.strip().upper()
        if j not in ("K","F"):
            raise ValueError("Hibás input!")

        s= int(s)
        o= int(o)

        if self.t[s][o]!="#":
            return False

        return self.Szabalyos(j,s,o)


#---------------------------------------------
import sys

# A program indításakor megadható a táblafájl neve a parancssorban: reversi.py allas2.txt
fname= sys.argv[1] if len(sys.argv)==2 else "allas.txt"

T= Tabla(fname)   # 4.feladat

print("\n5. feladat: A betöltött tábla:",fname)
T.Megjelenit()

print("\n6. feladat: Összegzés")
print("\tKék korongok száma: {}\n\tFehér korongok száma: {}\n\tÜres mezők száma: {}\n".format(T.Megszamlal("K"), T.Megszamlal("F"),T.Megszamlal("#")) )

print("\n8. feladat: ",end="")
if T.inpVanForditas():
    print("\tVan fordítás!")
else:
    print("\tNincs fordítás!")

print("\n9. feladat: ",end="")
if T.inpSzabalyos():
    print("\tSzabályos lépés!")
else:
    print("\tA lépés nem szabályos!")

#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben

