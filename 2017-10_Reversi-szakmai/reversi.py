#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# reversi.py
# Érettségi feladat: 2017. október, Reversi
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2017

class Tabla:

    def __init__(self, fname):
        """ 1.,2.,3. feladat """
        self.t= []
        with open(fname) as ff:
            for line in ff:
                line= line.strip()
                self.t.append(list(line))
        #print(self.t)    # teszt


    def Megjelenit(self):
        """ 5. feladat """
        for sor in self.t:
            print("\t"+"".join(sor))


    def Megszamlal(self,mit):
        """ 6. feladat """
        count=0
        for sor in self.t:
            count+= sor.count(mit)
        return count


    def VanForditas(self, jatekos, sor, oszlop, iranySor, iranyOszlop):
        """ 7. feladat """
        if self.t[sor][oszlop]!="#":
            return False

        aktSor= sor + iranySor
        aktOszlop= oszlop + iranyOszlop
        ellenfel= "K"
        if jatekos=="K":
            ellenfel= "F"

        nincsEllenfel= True

        while aktSor>=0 and aktSor<8 and aktOszlop>=0 and aktOszlop<8 and self.t[aktSor][aktOszlop]==ellenfel:
        # ***Lásd a megjegyzést alább!
            aktSor= aktSor + iranySor
            aktOszlop= aktOszlop + iranyOszlop
            nincsEllenfel= False

        if nincsEllenfel or aktSor<0 or aktSor>7 or aktOszlop<0 or aktOszlop>7 or self.t[aktSor][aktOszlop]!=jatekos:
            return False

        return True


    def inpVanForditas(self):
        """ Segédfgv a 7. feladathoz """
        j,s,o,irs,iro= input("[ jatekos;sor;oszlop;iranySor;iranyOszlop ] = ").split(";")
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
        s= int(s)
        o= int(o)

        if self.t[s][o]!="#":
            return False

        return self.Szabalyos(j,s,o)


#---------------------------------------------

T= Tabla("allas.txt")   # 4.feladat

print("\n5. feladat: A betöltött tábla")
T.Megjelenit()

print("\n6. feladat: Összegzés")
print("\tKék korongok száma: {}\n\tFehér korongok száma: {}\n\tÜres mezők száma: {}\n".format(T.Megszamlal("K"), T.Megszamlal("F"),T.Megszamlal("#")) )

print("\n8. feladat: ",end="")
if T.inpVanForditas():
    print("\tVan fordítás!")

print("\n9. feladat: ",end="")
if T.inpSzabalyos():
    print("\tSzabályos lépés!")

#*** A feladat kiírásában az algoritmus ezen sora hibás:
#  Ciklus amíg (aktSor>0 és aktSor<8 és aktOszlop>0 és aktOszlop<8 és t[aktSor, aktOszlop]=ellenfel)
#  Hibás eredményt ad például az allas2.txt esetén a 8. feladatban az "F;0;0;0;1" értékekkel.

#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben

