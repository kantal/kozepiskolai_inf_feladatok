#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# 3dik_feladat.py
# A 3. feladat megoldásának egy változata
# Érettségi feladat: 2018. május, Társalgó
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2018

#--- 1. feladat ---
ajtó=[]
with open("ajto.txt") as ff:
    for sor in ff:
        sor=sor.strip()
        if sor:
            óra,perc,személy,irány = sor.split()
            ajtó.append( (int(óra),int(perc),int(személy),irány) )


#--- A 3. feladat ---
print("--- 3. feladat dictionary-vel ---")
# Most nem tételezük fel az azonosítókról, hogy az [1-100] tartományba esnek.
áthaladás={}    # dictionary
for (óra,perc,személy,irány) in ajtó:
    áthaladás[személy]= áthaladás.get(személy,0)+1

print(áthaladás)    # szemrevételezés
áthalista= sorted(áthaladás.items())     # [ (személy1,eset1), (sz2,e2), ... ]
print()
print(áthalista)    # szemrevételezés

with open("dict_athaladas.txt","w") as ff:
    for személy, eset in áthalista:
        ff.write("{} {}\n".format(személy,eset))

# MEGJEGYZÉS:
# A sorba rendezés miatt fontos, hogy a "személy" int típusú és nem karakterlánc, mert különben
# például az "5" azonosítót "005"-re kellene bővíteni.
        

#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben

