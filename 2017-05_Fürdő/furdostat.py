#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# furdostat.py
# Érettségi feladat: 2017. május, Fürdő
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2017


#--- 1. feladat ---
print("\n1. feladat: Az adatok beolvasása.")

fürdőadat=[]    # Az adatok tárolására.
with open("furdoadat.txt") as ff:
    
    # [
    #   [azonosító_1,   [részleg, irány, óra,perc,mp], [részleg, irány, óra,perc,mp], ...],
    #   [azonosító_2,   [részleg, irány, óra,perc,mp], [részleg, irány, óra,perc,mp], ... ],
    #   ...
    # ]
    utolsó_azonosító=None
    utolsó_adat=None
    for sor in ff:
        
        azonosító, részleg, irány, óra,perc,mp= sor.split()
        
        if azonosító != utolsó_azonosító:
            if utolsó_adat:
                fürdőadat.append( utolsó_adat )
            utolsó_adat=[ azonosító ]
            utolsó_azonosító= azonosító

        utolsó_adat.append( [ int(részleg),int(irány),int(óra),int(perc),int(mp) ] )

    if utolsó_adat:
        fürdőadat.append( utolsó_adat)


#--- 2. feladat ---
print("\n2. feladat: ")
Öltöző,Uszoda,Szauna,Medence,Strand= 0,1,2,3,4
Be,Ki= 0,1

részleg, irány, óra,perc,mp = fürdőadat[0][1]
print("Az első vendég {}:{}:{}-kor lépett ki az öltözőből.".format(óra,perc,mp))

részleg, irány, óra,perc,mp = fürdőadat[-1][1]
print("Az utolsó vendég {}:{}:{}-kor lépett ki az öltözőből.".format(óra,perc,mp))

        
#--- 3. feladat ---
print("\n3. feladat: ")

egyrészlegesek=0

# Indexelős megoldás:
#for index in range(len(fürdőadat)):
#    if len(fürdőadat[index])-1 == 4:
#        egyrészlegesek+=1

# Egy pythonosabb megoldás:
# A 'fürdőadat' kettőnél több elemű "rekordokból" áll. Ezért a 'for azonosító, adatsor in fürdőadat:' hibás lenne.
# Ám '*' miatt az 'adatsor' egy lista lesz, amibe az első elem után következők mind beömlesztésre kerülhetnek.
for azonosító, *adatsor in fürdőadat:
    if len(adatsor)==4:         # öltözőbe/ből, az egyetlen részlegbe/ből
        egyrészlegesek+=1
    
print("A fürdőben {} vendég járt csak egy részlegen.".format(egyrészlegesek))


#--- 4. feladat ---
print("\n4. feladat:")

def ópm(ó,p,mp):
    return ó*3600+60*p+mp
    
tartamok=[]     # [ [azonosító,időtartam], ... ]
for azonosító, *adatsor in fürdőadat:
    
    krészleg, kirány, kó,kp,kmp = adatsor[0]       # kilépés az öltözőből
    brészleg, birány, bó,bp,bmp = adatsor[-1]      # belépés az öltözőbe
    tartamok.append( [azonosító, ópm(bó,bp,bmp)-ópm(kó,kp,kmp)] )

azonosító, tartam= max( tartamok, key=lambda a_t: a_t[1] )

print("A legtöbb időt eltöltő vendég:\n{}. vendég {}:{}:{}".format(azonosító, tartam//3600, (tartam%3600)//60, tartam%60) )


#--- 5. feladat ---
print("\n5. feladat:")

érk_stat= [0,0,0]        
intervallumok= [ (ópm(6,0,0),ópm(9,0,0)), (ópm(9,0,0),ópm(16,0,0)), (ópm(16,0,0),ópm(20,0,0)) ]

for azonosító, *adatsor in fürdőadat:
    
    részleg, irány, kó,kp,kmp = adatsor[0]
    időpont= ópm(kó,kp,kmp)
    
    for index, (kezdet,vég) in enumerate(intervallumok):
        if kezdet<=időpont<vég:
            érk_stat[index]+= 1

print("6-9 óra között {} vendég\n9-16 óra között {} vendég\n16-20 óra között {} vendég".format(*érk_stat))  # a '*' szétbontja a listát
#print("6-9 óra között {} vendég\n9-16 óra között {} vendég\n16-20 óra között {} vendég".format( érk_stat[0], érk_stat[1], érk_stat[2]) )  


#--- 6. feladat ---
print("\n6. feladat: Az adatok kiírása.")

with open("szauna.txt","w") as ff:
    
    for azonosító, *adatsor in fürdőadat:
        
        szaunaidők= [ ópm(kó,kp,kmp)  for részleg, irány, kó,kp,kmp in adatsor if részleg==Szauna ]
        szumma= sum(szaunaidők[1::2]) - sum(szaunaidők[0::2])
        if szumma:
            ff.write("{} {:02}:{:02}:{:02}\n".format(azonosító,szumma//3600, (szumma%3600)//60, szumma%60))
        

#--- 7. feladat ---
print("\n7. feladat:")
helyiségkód= [Uszoda,Szauna,Medence,Strand]
hstat= [0]*len(helyiségkód)

for azonosító, *adatsor in fürdőadat:
    
    for index,hk in enumerate(helyiségkód):

        for i in range(len(adatsor)):    
            if hk==adatsor[i][0]:          # 'részleg'
                hstat[index]+=1
                break
    
print("Uszoda: {}\nSzaunák: {}\nGyógyvizes medencék: {}\nStrand: {}".format(*hstat) ) 


#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben


