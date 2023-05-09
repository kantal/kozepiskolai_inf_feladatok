#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# 6dik_feladat.py
# Érettségi feladat: 2018. május, Fogadóóra
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2018

#--- 1. feladat ---
print("\n1. feladat: Az adatok beolvasása")
#minta: Csorba Ede 16:30 2017.10.28-18:48
adatok=[]
with open("fogado.txt") as ff:
    for sor in ff:
        sor=sor.strip()
        if sor:
            vnév,knév,időpont,fogidő= sor.split()
            adatok.append( ( (vnév+" "+knév).title(), időpont, fogidő) )
            

#--- 6. feladat ---
print("\n6. feladat")
# A fogadónap 16:00-tól 18:00-ig.
tanár= "Barna Eszter"
#tanár= "Neumann Nikolett"      # tesztelésre

# A foglalható időpontok:
időpontok={ "{:02d}:{:02d}".format(idő//60,idő%60):False  for idő in range(16*60,18*60,10) }
print(időpontok)

for név,időpont,fogidő in adatok:
    if név == tanár:
        időpontok[időpont]= True    # foglalt

# A könyvtári elemek sorrendjében nem lehetünk biztosak, ezért rendezést végzünk:
időpontok= sorted( időpontok.items())   # Ez már egy rendezett lista.
print("\n",időpontok)      

utolsó_foglalt=None
for időpont,foglalt in időpontok:
    if not foglalt:
        print(időpont)  # A szabadidő kiírása
    else:
        utolsó_foglalt= időpont

ótáv,ptáv= utolsó_foglalt.split(":")
itáv= int(ótáv)*60+int(ptáv)+10
print("{} legkorábban távozhat: {:02d}:{:02d}".format(tanár,itáv//60,itáv%60) )


    
#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben

