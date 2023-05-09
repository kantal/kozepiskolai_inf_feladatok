#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# metjelentés.py
# Érettségi feladat: 2020. május, Meteorológia
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2020

#--- 1. feladat ---
mhelyek= {}   # település --> napló

with open("tavirathu13.txt") as ff:
    # BP 0300 32007 21
    for sor in ff:

        sor= sor.strip()
        if not sor:
            continue
        település, óp, szél, hőm= sor.split()
        mhelyek.setdefault(település,[]).append( (óp, szél,int(hőm)) )

#print(*mhelyek.items(), sep="\n -->")   # szemrevételezés

#--- 2. feladat ---
település= input("2. feladat\nAdja meg egy település kódját! Település: ").strip().upper()
idő= mhelyek[település][-1][0]

print(f"Az utolsó mérési adat a megadott településről {idő[:2]}:{idő[2:]}-kor érkezett.")

#--- 3-4-5. feladat ---
# 3.feladat
napi_maxhőm= -1 # a feladat szerint az értékek nem negatívak
napi_minhőm= 500
# Az alábbi változókat itt csak a rend kedvéért nevezzük meg előre:
#napi_maxhőm_telep= napi_maxhőm_időpont= None
#napi_minhőm_telep= napi_minhőm_időpont= None

# 4.feladat
szélcsend= []

# 5. feladat
órák= ["01", "07", "13", "19"]
dstat= {}   # óra --> órás szumma

for település, napló in mhelyek.items():

        dhőm= {}       # 6. feladat
        maxhőm, minhőm= -1,500
        #maxhőm_időpont= minhőm_időpont= None    # csak a rend kedvéért
        n=0

        for időpont, szél, hőm in napló:

            if hőm > maxhőm:    # 3.feladat
                maxhőm= hőm
                maxhőm_időpont= időpont

            if hőm < minhőm:    # 3.feladat
                minhőm= hőm
                minhőm_időpont= időpont

            if szél=="00000":        # 4.feladat
                szélcsend.append( (időpont,település) )

            óra= időpont[:2]
            if óra in órák:
                n+= 1
                dhőm[óra]= dhőm.get(óra,0) + hőm

        átlag= round(sum(dhőm.values())/n) if len(dhőm)==len(órák) else "NA"    # 5. feladat
        dstat[település]= (átlag, maxhőm-minhőm)    # 5. feladat

        # Az összes települést figyelembe vevő számítások:
        if maxhőm > napi_maxhőm:
            napi_maxhőm= maxhőm
            napi_maxhőm_telep, napi_maxhőm_időpont= település, maxhőm_időpont

        if minhőm < napi_minhőm:
            napi_minhőm= minhőm
            napi_minhőm_telep, napi_minhőm_időpont= település, minhőm_időpont

print("3. feladat")
print(f"A legalacsonyabb hőmérséklet: {napi_minhőm_telep} {napi_minhőm_időpont[:2]}:{napi_minhőm_időpont[2:]} {napi_minhőm} fok.")
print(f"A legmagasabb hőmérséklet: {napi_maxhőm_telep} {napi_maxhőm_időpont[:2]}:{napi_maxhőm_időpont[2:]} {napi_maxhőm} fok.")


print("4. feladat")
if not szélcsend:
    print("Nem volt szélcsend a mérések idején.")
else:
    szélcsend.sort()    # időrendbe tesszük
    for időpont,település in szélcsend:
        print(f"{település} {időpont[:2]}:{időpont[2:]}")


print("5. feladat")
for település, (átlag, ingadozás) in dstat.items():

    if átlag != "NA":
        print(f"{település} Középhőmérséklet: {átlag}; Hőmérséklet-ingadozás: {ingadozás}")
    else:
        print(f"{település} NA; Hőmérséklet-ingadozás: {ingadozás}")


#--- 6. feladat ---
for település, napló in mhelyek.items():

    s= település+"\n"
    for időpont, szél, hőm in napló:

        s+= f"{időpont[:2]}:{időpont[2:]} " + int(szél[3:])*"#" + "\n"

    with open(település+".txt", "w") as ff:
            ff.write(s)

print("6. feladat\nA fájlok elkészültek.")

#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben
