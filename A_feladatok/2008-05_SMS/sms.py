#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# sms.py
# Érettségi feladat: 2008. május, SMS
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2018

#--- 1. feladat ---
print("\n1. feladat: Az adatok beolvasása.")
smsadat=[]
memkapacitás=10
with open("sms.txt") as ff:
    ff.readline()   # Átugorjuk/beolvassuk az első sort. Az sms-ek számát nem tároljuk el, mert nincs rá szükségünk. 
    
    # A 3.feladathoz
    minhossz,minindex= 200,-1
    maxhossz,maxindex= 0,-1
    # A 4.feladathoz:
    hosszcímke=("1-20", "21-40", "41-60", "61-80", "81-100")
    hossz_stat=[0]*5
    # Az 5.feladathoz:
    időszak=[0]*24 
    # A 6. feladathoz:
    barátnő_tsz="123456789"
    hívásidők=[]
    
    for index,sor in enumerate(ff): # A fájl 2. sorától folytatódik az olvasás, de az index 0-tól indul ebben a 'for' ciklusban.
        if not index%2:  
            # Az adatok tárolása:
            óra,perc,telszám= sor.split()
            óra,perc= int(óra),int(perc)
            smsadat.append( [óra,perc,telszám] )
            
            # 5.feladat:
            időszak[óra]+=1
            # 6. feladat:
            if telszám==barátnő_tsz:
                hívásidők.append( (óra,perc) )
            
        else:
            # Az adatok tárolása:
            szöveg= sor.strip()
            smsadat[-1].append(szöveg)  # [óra,perc,telszám] --> [óra,perc,telszám,szöveg]
            
            # 3. feladat:
            h=len(szöveg)
            if h < minhossz:
                minhossz,minindex= h,index//2
            if h > maxhossz:
                maxhossz,maxindex= h,index//2
            # 4. feladat:
            hossz_stat[ (h-1)//20 ]+= 1


#print(smsadat) # szemrevételezés

#--- 2. feladat ---
# A feladat kiírása szerint az adatok időrendi sorrendben vannak.
friss_index= min(memkapacitás,len(smsadat))-1
print("\n2. feladat\nA legfrissebb üzenet: '{}'".format(smsadat[friss_index][3]))

#--- 3. feladat ---
print("\n3. feladat")

#print("A legrövidebb üzenet:",smsadat[minindex][0],smsadat[minindex][1],smsadat[minindex][2],smsadat[minindex][3])  # indexeléssel

#minóra,minperc,mintelszám,minszöveg= smsadat[minindex]  # szétbontva
#print("A legrövidebb üzenet:",minóra,minperc,mintelszám,minszöveg)

print("A legrövidebb üzenet:", *smsadat[minindex]) # 'szétrobbantva'

print("A leghosszabb üzenet:", *smsadat[maxindex]) 

#--- 4. feladat ---
print("\n4. feladat")

for index,érték in enumerate(hossz_stat):
    print(hosszcímke[index],érték)

#--- 5. feladat ---
print("\n5. feladat")

díjas=0
for db in időszak:
    if db > memkapacitás:
        díjas+=db-memkapacitás
print("A szolgáltatót",díjas,"sms miatt kellene felhívni.")

#--- 6. feladat ---
print("\n6. feladat")

if len(hívásidők) < 2:
    print("nincs elegendő üzenet")
else:
    hívásidők.sort()
    maxtartam=0
    előző= hívásidők[0][0]*60+hívásidők[0][1]
    for index in range(1,len(hívásidők)):
        időpont= hívásidők[index][0]*60+hívásidők[index][1]
        tartam= időpont-előző
        if tartam > maxtartam:
            maxtartam= tartam
        előző= időpont

print("A leghosszabb időtartam két hívás között:", maxtartam//60,"óra",maxtartam%60,"perc")
            
#--- 7. feladat ---
print("\n7. feladat: Adja meg az üzenet adatait!")
óra= int(input("óra: "))
perc= int(input("perc: "))
telszám= input("telefonszám: ").strip()
szöveg= input("szöveg: ").strip()
smsadat.append( [óra,perc,telszám,szöveg] )
print(smsadat)

#--- 8. feladat ---
print("\n8. feladat: Kiírás fájlba.")

def bubirendtelszám(smsek):
    sd=smsek[:]     # smsek.copy()
    N= len(sd)
    for n in range(N):
        for k in range(1,N-n):
            if sd[k-1][2] > sd[k][2]:
                csere=sd[k-1]
                sd[k-1]=sd[k]
                sd[k]=csere
    return(sd)

#rendmem= bubirendtelszám(smsadat)
rendmem= sorted(smsadat, key= lambda tétel: tétel[2])   # ide nem kell a 'bubirendtelszám()'

with open("smski.txt","w") as ff:
    előzőtsz=None
    for óra,perc,telszám,szöveg in rendmem:
        if telszám!=előzőtsz:
            ff.write(telszám+"\n")
            előzőtsz=telszám
        ff.write(" {:02d}:{:02d} {}\n".format(óra,perc,szöveg))
    

#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben


