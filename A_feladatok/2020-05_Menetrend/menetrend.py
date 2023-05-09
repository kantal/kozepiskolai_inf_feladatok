#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# menetrend.py
# Érettségi feladat: 2020. május, Menetrend
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2020

#--- 1. feladat ---
#1	0	5	45	I
#1	1	6	0	E
# vonatszám állomásszám óra perc Indulás/Érkezés
dvonatok= {}    # vonatszám --> napló
with open("vonat.txt") as ff:
    for sor in ff:
        sor= sor.strip()
        if not sor:
            continue
        vonat, állomás, óra, perc, ie= sor.split()

        dvonatok.setdefault(vonat,[]).append( (állomás,int(óra)*60+int(perc),ie) )
        # (állomásszám, időpont percben, E vagy I) (str,int,str)

        # A setdefault() helyett "hagyományos" megoldással:
        #if vonat not in dvonatok:
        #        dvonatok[vonat]= []
        #napló= dvonatok[vonat]
        #napló.append( (állomás,int(óra)*60+int(perc),ie) )


#print(dvonatok.items()) # szemrevételezés
#print(*dvonatok.items(),sep="\n") # szemrevételezés

#--- 2. feladat ---
# I ÉI ÉI ... ÉI É  # 1+ (len-2)/2 +1= 1+len/2
print(f"\n2. feladat\nAz állomások száma: {1+len(dvonatok['1'])//2}\nA vonatok száma: {len(dvonatok)}")

#--- 3. feladat ---
tartam= 0
tvonat= tállomás= None
for vonat,napló in dvonatok.items():

    for i in range(1,len(napló)-1,2):
        dt= napló[i+1][1] - napló[i][1]
        if dt > tartam:
            tartam= dt
            tvonat, tállomás= vonat, napló[i][0]

print(f"\n3. feladat\nA(z) {tvonat}. vonat a(z) {tállomás}. állomáson {tartam} percet állt.")

#--- 4. feladat ---
print("\n4. feladat")
vsz= input("Adja meg egy vonat azonosítóját! ").strip()
ó,p= input("Adjon meg egy időpontot (óra perc)! ").split()
időpont= int(ó)*60 + int(p)

#--- 5. feladat ---
print("\n5. feladat")
előírt_menetidő= 2*60 + 22
srövidebb= "A(z) {}. vonat útja {} perccel rövidebb volt az előírtnál."
selőírt= "A(z) {}. vonat útja pontosan az előírt ideig tartott."
shosszabb= "A(z) {}. vonat útja {} perccel hosszabb volt az előírtnál."

eltérés= előírt_menetidő - dvonatok[vsz][-1][1] + dvonatok[vsz][0][1]
if not eltérés :
    print(selőírt.format(vsz))
elif eltérés < 0:
    print(shosszabb.format(vsz,-eltérés))
else:
    print(srövidebb.format(vsz,eltérés))

#--- 6. feladat ---
fname= "halad" + vsz + ".txt"
with open(fname,"w") as fout:

    for állomás, perc, irány in dvonatok[vsz]:
        if irány=="E":
            fout.write( f"{állomás}. állomás: {perc//60}:{perc%60}\n" )

#--- 7. feladat ---
print("\n7. feladat")

for vonat in range(1,len(dvonatok)+1):

    for állomás, perc, irány in dvonatok[str(vonat)]:

        if irány == "E":
            if időpont < perc:
                print(f"A(z) {vonat}. vonat a(z) {int(állomás)-1}. és a(z) {állomás}. állomás között járt.")
                break

        elif időpont <= perc:   # I
            if állomás != "0":
                print(f"A(z) {vonat}. vonat a(z) {állomás}. állomáson állt.")
            break


#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben

