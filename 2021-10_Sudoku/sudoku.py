#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# sudoku.py
# Érettségi feladat: 2021. október, Sudoku
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2022

DEBUG=True
#DEBUG=False

#--- 1. feladat
print( "1. feladat")

fsudoku= input( "Adja meg a bemeneti fájl nevét! ").strip()
sor_bekért= int( input( "Adja meg egy sor számát! (1-9) ")) -1    # Az index 0-tól számítandó!
oszlop_bekért= int( input( "Adja meg egy oszlop számát! (1-9) ")) -1

# 2. feladat
tábla= []
lépések= []

with open( fsudoku) as ff:

    sorszám= 0
    for sor in ff:

        sor= sor.strip()
        if not sor:
            continue

        sorszám += 1
        sor= [ int(sz) for sz in sor.split() ]
        if sorszám <= 9:
            tábla.append( sor)
        else:
            lépések.append( sor)


if DEBUG:   # szemrevételezés
    print( *tábla, sep="\n")
    print( *lépések, sep="\n")


#---  3. feladat
print( "\n3. feladat")

szám= tábla[ sor_bekért][ oszlop_bekért]

if szám != 0:
    print( f"Az adott helyen szereplő szám: {szám}")
else:
    print( "Az adott helyet még nem töltötték ki.")

rt_nOszlop, rt_nSor= 3, 3   # egy résztábla mérete
rt_per_sor= 3   # a résztáblák száma egy sorban


def résztábla_sorszáma( sor, oszlop):

    """ Megadja, hogy a megdott sor-oszlop pozíció melyik résztáblába esik.

    sor: int, 0-tól indul, sorpozíció a nagy táblában
    oszlop: int, 0-tól indul, oszloppozíció a nagy táblában
    globals: rt_nOszlop, rt_nSor, rt_per_sor

    Return: int, a bennfoglaló résztábla sorszáma, 0-tól indul
    """

    # a résztábla koordinátái
    rt_oszlop=  oszlop // rt_nOszlop
    rt_sor=     sor // rt_nSor

    return  rt_sor * rt_per_sor +  rt_oszlop   # a sorszám 0-tól számítva


print( f"A hely a(z) { résztábla_sorszáma( sor_bekért, oszlop_bekért) + 1 }. résztáblázathoz tartozik.")


#--- 4. feladat
print( "\n4. feladat")

arány= 100 * sum( s.count(0) for s in tábla) / 81
print( f"Az üres helyek aránya: {arány:.1f}%" )


#---  5. feladat
print( "\n5. feladat")

def ellenőrzés( tb, lépés):
    """
    tb: Sudoku tábla
    lépés: pl. [9,1,2]  szám, sor és oszlop, ahol az utóbbi kettő
          1-től számítódik.

    globals: rt_nOszlop, rt_nSor
    """

    szám, sor, oszlop = lépés
    print( f"A kiválasztott sor: {sor} oszlop: {oszlop} a szám: {szám}")

    sor = sor - 1   # az index 0-tól indul
    oszlop = oszlop - 1

    if tb[sor][oszlop] != 0:
        print( "A helyet már kitöltötték.\n")
        return

    if szám in tb[sor]:
        print( "Az adott sorban már szerepel a szám.\n")
        return

    for i in range(9):
        if tb[i][oszlop] == szám:
            print( "Az adott oszlopban már szerepel a szám.\n")
            return

    sk= (sor // rt_nSor) * rt_nSor           # A résztábla bal-felső (kezdő) elemének sorpozíciója
    ok= (oszlop // rt_nOszlop) * rt_nOszlop  # és oszloppozíciója.

    for s in range(3):
        for o in range(3):
            if tb[ sk+s][ ok+o] == szám:
                print( "Az adott résztáblázatban már szerepel a szám.\n")
                return

    print( "A lépés megtehető.\n")


for nso in lépések:
    ellenőrzés( tábla, nso)

#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben

