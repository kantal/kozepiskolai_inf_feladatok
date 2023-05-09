#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# cbradio.py
# ÁGAZATI érettségi feladat: 2019. október, CB-rádió
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2019

#--- 1-2. feladat ---
class Napló:

    def __init__(self,fname):
        """
            fname: a naplófájl neve elérési úttal
        """
        with open(fname) as ff:

            next(ff)    # átugorjuk az első sort, amely a mezőneveket tartalmazza
            self.adás4_1=False    # Volt-e olyan sofőr, aki egy percen belül pontosan 4 adást indított.
            self.lnapló=[]  # lista, amelybe (óra,perc,adásdb,név) sokaságokat (tuple) tárolunk
            self.dnapló={}  # szótár; név-->adásainak_összes_száma
            for line in ff:
                
                óra,perc,adásdb,név= line.split(";")
                óra,perc,adásdb= int(óra),int(perc),int(adásdb)
                név=név.strip()     # levágjuk a sorvégjelet
                self.lnapló.append( (óra,perc,adásdb,név) )
                self.dnapló[név]= self.dnapló.get(név,0)+adásdb
                
                if not self.adás4_1 and adásdb==4:     
                        self.adás4_1= True

    def bejegyzések_száma(self):
        return len(self.lnapló)

    def volt_sofőr4_1(self):
        return self.adás4_1

    def sofőr_össz_cb(self,név):
        return self.dnapló.get(név, None)

    def sofőrök_száma(self):
        return len(self.dnapló)

    def legtöbb_adás(self):
        return max(self.dnapló.items(),key=lambda névdb: névdb[1])

#---
taxicb= Napló("cb.txt") 

#--- 3. feladat ---
print(f"3. feladat: Bejegyzések száma: {taxicb.bejegyzések_száma()} db")

#--- 4. feladat ---
print(f"4. feladat:", "Volt" if taxicb.volt_sofőr4_1() else "Nem volt", "négy adást indító sofőr.")

#--- 5. feladat ---
megadott_név=input("5. feladat: Kérek egy nevet: ")
alkalom= taxicb.sofőr_össz_cb(megadott_név)
if alkalom==None:
    print("\tNincs ilyen nevű sofőr!")
else:
    print(f"\t{megadott_név} {alkalom}x használta a CB-rádiót.")    

#--- 6. feladat ---
def ÁtszámolPercre(óra,perc):
    return óra*60+perc

#--- 7. feladat ---
with open("cb2.txt","w") as fout:
    
     fout.write("Kezdes;Nev,AdasDb\n")
     for (óra,perc,adásdb,név) in taxicb.lnapló:
         fout.write(f"{ÁtszámolPercre(óra,perc)};{név};{adásdb}\n")
         
#--- 8. feladat ---
print(f"8. feladat: Sofőrök száma: {taxicb.sofőrök_száma()} fő")

#--- 9. feladat ---
sofőr,adások= taxicb.legtöbb_adás()
print(f"9. feladat: Legtöbb adást indító sofőr\n\tNév: {sofőr}\n\tAdások száma: {adások} alkalom")

#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben

