#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# fogado.py
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
            adatok.append( (vnév+" "+knév, időpont, fogidő) )
            
#--- 2. feladat ---
print("\n2. feladat")
print( "Foglalások száma:",len(adatok))

#--- 3. feladat ---
print("\n3. feladat")
# Nem lenne fontos, de ha több szóköz lenne, akkor azokat "lenyeljük".
megadott_vnév, megadott_knév= input("Adjon meg egy nevet: ").split()
megadott_név= megadott_vnév+" "+megadott_knév
foglalások=0
for név,időpont,fogidő in adatok:
    if név.lower() == megadott_név.lower():
        foglalások+=1
        
if foglalások:
    print(megadott_név,"néven", foglalások, "időpontfoglalás van.")
else:
    print("A megadott néven nincs időpontfoglalás.")

    
#--- 4. feladat ---
print("\n4. feladat")
megadott_óra, megadott_perc= input("Adjon meg egy érvényes időpontot (pl. 17:10): ").split(":")
megadott_óra, megadott_perc= megadott_óra.strip(), megadott_perc.strip()  
fkimenet= megadott_óra+megadott_perc+".txt"
megadott_időpont= megadott_óra+":"+megadott_perc
foglaltak=[]

for név,időpont,fogidő in adatok:
    if megadott_időpont == időpont:
        foglaltak.append(név)

foglaltak.sort()
with open(fkimenet,"w") as ff:
    for tanár in foglaltak:
        print(tanár)
        ff.write(tanár+"\n")    

            
#--- 5. feladat ---
print("\n5. feladat")

def hasonlít(tétel):
    #return tétel[2]
    név,időpont,fogidő=tétel
    return fogidő
    
név,időpont,minfoglalás= min(adatok,key=hasonlít)
#név,időpont,minfoglalás= min(adatok,key=lambda tétel: tétel[2])

print("Tanár neve: {}\nFoglalt időpont: {}\nFoglalás ideje: {}".format(név,időpont,minfoglalás) )


#--- 6. feladat ---
print("\n6. feladat")
# A fogadónap 16:00-tól 18:00-ig.

def csindex(időpont):
    """ Indexet állít elő az 'óó:pp' karakterláncból. """
    ó,p= időpont.split(":")
    ó,p= int(ó),int(p)
    return ((ó-16)*60+p)//10
    
def csidőpont(index):
    """ 'óó:pp' formátumú karakterláncot állít elő az indexből. """
    időpont=10*index+16*60
    return "{}:{:02d}".format(időpont//60,időpont%60)
    
időpontok=[0]*12    # A foglalható időpontoknak felel meg: 0->16:00, 1->16:10, ... 11->17:50

for név,időpont,fogidő in adatok:
    if név.lower()=="barna eszter":
        időpontok[ csindex(időpont) ]=1

utolsó_foglalt=None
for index,foglalt in enumerate(időpontok):
    if not foglalt:
        print( csidőpont(index) )
    else:
        utolsó_foglalt= index
        
print("Barna Eszter legkorábban távozhat:", csidőpont(utolsó_foglalt+1) )


    
#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben

