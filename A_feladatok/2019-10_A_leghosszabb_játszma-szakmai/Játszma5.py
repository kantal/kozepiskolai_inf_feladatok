#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# Játszma5.py
# ÁGAZATI érettségi feladat: 2019. október, A leghosszabb játszma
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2019

#--- 6. feladat ---
class Játék:

    def __init__(self,adogató,fogadó,állás):    # 6.abc

        self.adogató= adogató   
        self.fogadó= fogadó     
        self.állás= állás

    def Hozzáad(self,labdamenet):   # 6.d
        # labdamenet: 'A' vagy 'F'
        self.állás+= labdamenet
        
    def NyertLabdamenetekSzáma(self,adfog):   # 6.e
        # adfog: 'A' vagy 'F'
        return self.állás.count(adfog)
        
    """
    Függvény JátékVége(): logikai
        Változó nyertAdogató: egész
        Változó nyertFogadó: egész
        Változó különbség: egész
        nyertAdogató := NyertLabdamenetekSzáma(’A’)
        nyertFogadó := NyertLabdamenetekSzáma(’F’)
        különbség := AbszolútÉrték (nyertAdogató – nyertFogadó)
        Térj vissza (nyertAdogató >= 4 VAGY nyertFogadó >=4) ÉS (különbség >= 2)
    Függvény vége
    """
    def JátékVége(self):    # 6.f

        nyertAdogató= self.NyertLabdamenetekSzáma("A")
        nyertFogadó= self.NyertLabdamenetekSzáma("F")
        különbség= abs(nyertAdogató-nyertFogadó)
        return (nyertAdogató >= 4 or nyertFogadó >=4) and (különbség >= 2)

    def megnyerte(self):
        # a nyertes nevét adja vissza
        return self.adogató if self.NyertLabdamenetekSzáma("A") > self.NyertLabdamenetekSzáma("F") else self.fogadó

        
#--- 1-2. feladat ---
class Játszma:

    def __init__(self,no,fname,játékos1,játékos2):
        """
        no: A játszma sorszáma.
        fname: A játszma labdameneteit tartalmazó fájl.
        játékos1: A játszmát adogatással kezdő játékos neve.
        """
        self.no= no
        self.játékos1= játékos1
        self.játékos2= játékos2

        with open(fname) as ff:
            self.labdamenetek= [ c for c in ff.read() if c in "AF" ]

        #--- 8. feladat
        games=[ Játék(játékos1,játékos2,"") ]
        gm= games[-1]
        for m in self.labdamenetek:

            if gm.JátékVége():
                # új játékot kezdünk:
                games.append( Játék(gm.fogadó,gm.adogató,m) )
                gm= games[-1]
                
            else:
                gm.Hozzáad(m)
                
        self.játékok= games


    def lbdmntk_száma(self):
        return len(self.labdamenetek)
        
    def nyert_lbdmntk_A(self):
        return 100*self.labdamenetek.count('A') / len(self.labdamenetek)


    def max_nyert_sorozat_A(self):
        
        maxmenet= 0
        menet= 0
        for m in self.labdamenetek:
            if m=='A':
                menet+=1
            else:
                if menet>maxmenet:
                    maxmenet=menet
                menet=0
                
        if menet>maxmenet:
            maxmenet=menet
            
        return maxmenet


    def végeredmény(self):
        # Return: (j1,j2) a játékosok által nyert játékok száma
        j1=0
        for gm in self.játékok:

            if gm.megnyerte()==self.játékos1:
                j1+=1
                
        return j1, len(self.játékok)-j1

#---
# A játszma objektum létrehozása:
játszma5= Játszma(5,"labdamenetek5.txt","Isner","Mahut")

#--- 3. feladat ---
print("3. feladat: Labdamenetek száma:", játszma5.lbdmntk_száma())

#--- 4. feladat ---
print(f"4. feladat: Az adogató játékos {játszma5.nyert_lbdmntk_A()}%-ban nyerte meg labdameneteket.")

#--- 5. feladat ---
print("5. feladat: A leghosszabb sorozat:",játszma5.max_nyert_sorozat_A())

#--- 7. feladat ---
PróbaJáték= Játék("Mahut","Isner","FAFAA")
PróbaJáték.Hozzáad("A")
vége= "igen" if PróbaJáték.JátékVége() else "nem"
print(f"7. feladat: A próba játék\n\tÁllás: {PróbaJáték.állás}\n\tBefejeződött a játék: {vége}")

#--- 9. feladat ---
Isner,Mahut= játszma5.végeredmény()
print(f"9. feladat: Az 5. játszma végeredménye:\n\tMahut: {Mahut}\n\tIsner: {Isner}")


#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben

