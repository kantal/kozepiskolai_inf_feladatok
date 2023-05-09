#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# privát.py
# Program: Koós Antal, 2018

"""
 Egy Python objektumban minden változó publikus. És ez tervszerűen van így, azaz ez nem hiányossága a nyelvnek. Egy változó vagy metódus nem kívánt módosítását illetve kiolvasását több módon is jelezhetjük, bár teljességgel megakadályozni nem tudjuk.
( A programozás során "elvárható gondosságot" semmi sem pótolja, és még a más nyelvekben honos
'public' és 'privát' konstrukciók használata sem csodaszer.)

 Egy '_' jellel SZOKÁS jelölni a privátnak szánt változókat, pl.: _szöveg= "privát lennék, tartsd tiszteletben".
 A kettős '_'-sal jelzett változók valamivel védettebbek, mert az elérésük az osztályon kívülről csak trükkösen tehető meg.
"""

class Ügyosztály:

    __téma="bármi"
    
    def __init__(self):
        self._oldalszám= 100
        self.__szerző= "Hakapeci"

    def író(self):
        return self.__szerző.upper()  # Az objektumon belül korlátozás nélkül kiolvasható.

    def módosít(self,név):
        self.__szerző= név   # Az objektumon belül korlátozás nélkül átírható.

#print(Ügyosztály.__téma)   # Próbáld ki!
oo=Ügyosztály()
print(oo._oldalszám)        # Gond nélkül elérhető közvetlenül, de talán nem kellene :-)
#print(oo.__szerző)         # Próbáld ki!
print(oo.író())
oo.módosít("Móriczka")
#print(oo._Ügyosztály__szerző)   # 'Trükkös' elérés lehetséges, de ez már büntetendő :-)))
print(10*"_"+"\n")

""" 
 Az alábbiakban készítünk egy "privát", 'Titkosítandó' nevű változót, amit olvasni lehet, de  egyszerűen, "természetes" módon írni nem. Ehhez azonban már a __getattr__ és a __setattr__ speciális metódusokat is fel kell használnunk.
"""

class MC:
    
    def __init__(self):
        
        self.__Titkosítandó= "Nagyon titkos!"    # Csak olvasható lesz, úgy mint 'Titkosítandó'.
        

    def __getattr__(self,név):
        """ Akkor hívódik meg, amikor nincs 'név' nevű jellemzője az objektumnak. """
        # A 'Titkosítandó' lekérdezése esetén a '__Titkosítandó' értékét adjuk vissza.
        if név=="Titkosítandó":     
            return self.__Titkosítandó
        # Egyéb nem létező változó esetén a szokásos eljárás:
        raise AttributeError("'{}' objektumnak nincs ilyen jellemzője: '{}'".format(self.__class__,név))

            
    def __setattr__(self,név,value):
        """ Értékadásnál hívódik meg. """
        # Letitjuk a 'Titkosítandó' nevű változóhoz érték rendelését.
        # A  '__Titkosítandó' név tiltására nem feltétlen van szükség, de így megakadályozzuk, hogy
        # kívülről hasonló nevű jellemzőt lehessen készíteni: obi=MC(); obi.__Titkosítandó="valami"
        # Lásd még lentebb a '__Bizalmas' változót!
        if név in ["Titkosítandó", "__Titkosítandó"]:   
            raise AttributeError("Kísérlet 'privát' változó módosítására: '{}'".format(név))
        else:
            # Egyéb változónak történő értékadáshoz meghívjuk az objektum ősében lévő, eredeti értékadó metódust:
            super().__setattr__(név,value)


    def módosít(self):
        # Az osztályon belül elérhető a változó:
        self.__Titkosítandó= self.__Titkosítandó.upper()    


#---------------
#---- TESZT ----
#---------------

obi= MC()   
try:
    print(obi.__Titkosítandó)       # Az osztályon kívül "természetes módon" nem olvasható.
except AttributeError as esemény:
    print(esemény)

print(obi._MC__Titkosítandó)    # Trükkösen már elérhető.

print("Titkosítandó=",obi.Titkosítandó)     # Olvasható a 'szimulált Titkosítandó' változó
obi.módosít()                               # Osuzályon belüli módosítás.
print("Titkosítandó=",obi.Titkosítandó)     

try:
    obi.Titkosítandó="Nyílt titok"  # Kívülről nem módosítható és nem hozható létre a szimulált változó.
except AttributeError as esemény:
    print(esemény)

try:
    obi.__Titkosítandó="Nyílt titok"    # Nem hozható létre kívülről ez sem: '__Titkosítandó"
except AttributeError as esemény:
    print(esemény)


print()
# Az osztályhoz kívülről hozzáadni '_' jellel kezdődő nevű változókat valószínűleg "csúnya dolog":
obi.__Bizalmas=1      # Az osztályon kívül létrehozva nem módosul a név erre: obi._MC__Bizalmas
print(obi.__Bizalmas) # "simán" is elérhető.
obi._MC__Bizalmas=99  # Persze kívülről is létrehozhatunk ilyesmit, de ennek semmi köze az előző  '__Bizalmas' változóhoz.
print(obi._MC__Bizalmas)
print()

#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben


