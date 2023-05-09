#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# EletjatekGUI.py
# ÁGAZATI érettségi feladat: 2021. október, Életjáték, GUI
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2022

""" A feladatot a kiírás szerint Java vagy C# nyelven kellett megoldani,
    de mi most gyakorlásképpen Pythonban készítjük el.
"""

import tkinter as tk
from tkinter import ttk

win= tk.Tk()
win.title( "Életjáték-álláskészítő")

frm_main= ttk.Frame( win)

lbl1= ttk.Label( frm_main, text="Mátrix mérete [sor x oszlop]:" )
cbox_sor= ttk.Combobox( frm_main)
cbox_oszlop= ttk.Combobox( frm_main)
btn_üres= ttk.Button( frm_main, text="Üres mátrix létrehozása")
btn_mentés= ttk.Button( frm_main, text= "Állás mentése")
frm_mátrix= ttk.Frame( frm_main)

maxdim, mindim = 20, 5  # pixels

tkv_sor= tk.IntVar( value= maxdim)
cbox_sor[ "textvariable"]= tkv_sor
cbox_sor[ "values"]= list( range( mindim, maxdim+1))
cbox_sor[ "state"]= ["readonly"]

tkv_oszlop= tk.IntVar( value= maxdim)
cbox_oszlop[ "textvariable"]= tkv_oszlop
cbox_oszlop[ "values"]= list( range( mindim, maxdim+1))
cbox_oszlop[ "state"]= ["readonly"]

check_buttons= []

def callback_btn_üres():
    global check_buttons

    sor, oszlop = tkv_sor.get(), tkv_oszlop.get()

    if check_buttons:

        akt_sorok= len(check_buttons)
        akt_oszlopok= len(check_buttons[0])

        if sor == akt_sorok and oszlop == akt_oszlopok:

            for s in range(sor):
                for o in range(oszlop):
                    check_buttons[s][o][0].set( False)
            return

        for s in range( akt_sorok):
            for o in range( akt_oszlopok):
                check_buttons[s][o][1].destroy()

    check_buttons= []
    for s in range(sor):

        egy_sor= []
        for o in range( oszlop):

            tv= tk.BooleanVar( value= False)
            chkbtn= ttk.Checkbutton( frm_mátrix, variable= tv)
            chkbtn.grid( row= s, column= o)
            egy_sor.append( [tv, chkbtn] )

        check_buttons.append( egy_sor)


def callback_btn_mentés():

    if not check_buttons:
        return

    sor, oszlop = tkv_sor.get(), tkv_oszlop.get()
    fname= f"Eletjatek_{sor}x{oszlop}.txt"

    with open( fname, "w") as ff:

        for s in range(sor):

            egy_sor= [ "1" if check_buttons[s][o][0].get() else "0" for o in range(oszlop) ]
            egy_sor.append( "\n")
            ff.write( "".join( egy_sor) )


btn_üres[ "command"]= callback_btn_üres
btn_mentés[ "command"]= callback_btn_mentés


lbl1.grid( row=0, column=0)
cbox_sor.grid( row=0, column=1)
cbox_oszlop.grid( row=0, column=2)
btn_üres.grid( row=1, column=0)
btn_mentés.grid( row=1, column=2)
frm_mátrix.grid( row=2, column=0, columnspan=3)

cbox_sor["width"]= cbox_oszlop["width"]= 3  # characters

#frm_main.rowconfigure( 0, pad= 15)
frm_main.rowconfigure( 1, pad= 15 )     # pixels
frm_main.rowconfigure( 2, pad= 15, minsize= 100 )
frm_main["pad"]= 15
frm_main.grid()

win.mainloop()

#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben

