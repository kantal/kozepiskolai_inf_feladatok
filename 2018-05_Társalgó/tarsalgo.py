#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# tarsalgo.py
# Érettségi feladat: 2018. május, Társalgó
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2018

#--- 1. feladat ---
print("\n1. feladat: Az adatok beolvasása")
ajtó=[]
with open("ajto.txt") as ff:
    for sor in ff:
        sor=sor.strip()
        if sor:
            óra,perc,személy,irány = sor.split()
            ajtó.append( (int(óra),int(perc),int(személy),irány) )
            
#print(ajtó)    # szemrevételezés

#--- 2. feladat ---
print("\n2. feladat")
utolsó_kilépő=None

for (óra,perc,személy,irány) in ajtó:   # előrefelé keresünk
    if irány == "ki":
        utolsó_kilépő= személy

#for i in range(len(ajtó)-1,-1,-1):      # visszafelé is kereshetnénk
#    óra,perc,személy,irány= ajtó[i]
#    if irány == "ki":
#        utolsó_kilépő= személy
#        break   

#for (óra,perc,személy,irány) in reversed(ajtó):   # itt is visszafelé keresünk
#    if irány == "ki":
#        utolsó_kilépő= személy
#        break


print("Az első belépő:",ajtó[0][2],"\nAz utolsó kilépő:",utolsó_kilépő)


#--- 3. feladat ---
print("\n3. feladat: athaladas.txt írása")
# Kihasználjuk, hogy a feladat szerint az azonosítók tartománya 1-100.
# Mivel 0-ás személyi azonosító nincs, így az alábbi lista csak az [1,100] indextartományban fog változni.
áthaladás=[0]*101   
for (óra,perc,személy,irány) in ajtó:
    áthaladás[személy]+=1
    
with open("athaladas.txt","w") as ff:    
    for személy in range(1,len(áthaladás)):
        eset= áthaladás[személy]
        if eset:
            ff.write("{} {}\n".format(személy,eset))


#--- 4. feladat ---
print("\n4. feladat")
print("A végén a társalgóban voltak:",end=" ")
for személy in range(1,len(áthaladás)):
    if áthaladás[személy]%2:     
        print(személy,end=" ")

print()        

        
#--- 5. feladat ---
print("\n5. feladat")
létszám=0
létmax,óramax,percmax=0,0,0
for (óra,perc,személy,irány) in ajtó:
    if irány=="ki":
        létszám-=1
    else:
        létszám+=1
        if létszám > létmax:
            létmax,óramax,percmax=létszám,óra,perc

print("Például {}:{}-kor voltak a legtöbben a társalgóban.".format(óramax,percmax))      


#--- 6. feladat ---
print("\n6. feladat")
megadott_személy= int(input("Adja meg a személy azonosítóját! "))

#--- 7. feladat ---
print("\n7. feladat")

def tartam(bó,bp,kó,kp):
    """ Input: a be- és kilépés órája és perce. """
    return (kó-bó)*60+kp-bp
    
percek=0            # összesítés
bóra,bperc=0,0      # a belépés ideje
benn_van=False
for (óra,perc,személy,irány) in ajtó:
    if személy!=megadott_személy:
        continue
    if irány=="be":
        print("{}:{}".format(óra,perc),end="-")
        bóra,bperc=óra,perc
        benn_van=True
    else:
        print("{}:{}".format(óra,perc))
        percek+= tartam(bóra,bperc,óra,perc)
        benn_van=False

if benn_van:    # ha végül nem jött ki 
    percek+= tartam(bóra,bperc,15,0)        
print()        
    

#--- 8. feladat ---
print("\n8. feladat")
holtext= "a társalgóban volt" if benn_van else "nem volt a társalgóban"

print("A(z) {}. személy összesen {} percet volt bent, a megfigyelés végén {}.".format(megadott_személy,percek,holtext) )


#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben

