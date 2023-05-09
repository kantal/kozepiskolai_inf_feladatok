#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# Pars2012.py
# ÁGAZATI érettségi feladat: 2021. május, Kalapácsvetés, CLI
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2022

""" A feladatot a kiírás szerint Java vagy C# nyelven kellett megoldani,
    de mi most gyakorlásképpen Pythonban készítjük el.
"""


class Versenyző:

    def __init__( self, sor):

        # sor: Név;Csoport;NemzetÉsKód;D1;D2;D3
        #       A. G. Kruger;B;Egyesült Államok (USA);X;72,13;X
        #       ...
        #       Pars Krisztián;B;Magyarország (HUN);77,11;79,37;-

        self.Név, self.Csoport, nzkd, *self.s_dobások = sor.strip().split(";")

        self.Nemzet, self.Kód = nzkd.split("(")
        self.Nemzet= self.Nemzet.strip()
        self.Kód= self.Kód.rstrip(")")

        self.dobások= [ -1.0 if s == "X" else -2.0 if s == "-" else float( s.replace(",",".") ) for s in self.s_dobások ]

        self.Eredmény= max( self.dobások)


    def __str__( self):

        sd= ";".join( self.s_dobások)
        se= str( self.Eredmény).replace(".",",")

        return f"\tNév: {self.Név}\n\tCsoport: {self.Csoport}\n\tNemzet: {self.Nemzet}\n\tNemzet kód: {self.Kód}\n\tSorozat: {sd}\n\tEredmény: {se}"



#--
if __name__ == "__main__":

    f_selejtező= "Selejtezo2012.txt"

    with open( f_selejtező) as ff:

        next(ff)
        versenyzők= [ Versenyző(s) for s in ff ]

    # 5. feladat
    print( f"5. feladat: Versenyzők száma a selejtezőben: {len(versenyzők)} fő")

    # 6. feladat
    n78= sum( 1 for v in versenyzők if v.dobások[0] > 78 or v.dobások[1] > 78 )
    print( f"6. feladat: 78,00 méter feletti eredménnyel továbbjutott: {n78} fő")

    # 9. feladat
    versenyzők.sort( key=lambda v: v.Eredmény, reverse= True)

    nyertes= versenyzők[0]
    print( "9.feladat: A selejtező nyertese:" )
    print( nyertes)

    # 10. feladat
    f_döntős= "Dontos2012.txt"

    with open( f_döntős, "w") as ff:

        ff.write( "Helyezés;Név;Csoport;Nemzet;NemzetKód;Sorozat;Eredmény\n")
        for n in range(12):

            v= versenyzők[n]
            sorozat= ";".join( v.s_dobások)
            eredm= str(v.Eredmény).replace(".",",")
            ff.write( f"{n+1};{v.Név};{v.Csoport};{v.Nemzet};{v.Kód};{sorozat};{eredm}\n")

#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben
