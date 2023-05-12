#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# CsevegesGUI.py
# Szakmai érettségi feladat: 2022. október, Csevegés, GUI
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2023

""" A feladatot a kiírás szerint Java vagy C# nyelven kellett megoldani,
    de mi most gyakorlásképpen Pythonban készítjük el.
"""

import Cseveges
import tkinter as tk
from tkinter import ttk
import tkinter.scrolledtext as tktext

#--- Data
db= Cseveges.CsevDB( "csevegesek.txt", "tagok.txt")

#--- Widgets
win= tk.Tk()
win.title( "Csevegés GUI")
win.resizable( width=False, height=False)

frm= ttk.Frame( win)

lblKezdeményező= ttk.Label( frm, text="Kezdeményező" )
cboxNevek1= ttk.Combobox( frm, values= db.Tagok, state= "readonly")
cboxNevek1.current(0)

lblFogadó= ttk.Label( frm, text="Fogadó (partner)" )
cboxNevek2= ttk.Combobox( frm, values= db.Tagok, state= "readonly" )
cboxNevek2.current( len(db.Tagok)-1 )

lblCsevegések= ttk.Label( frm, text="Csevegések")
textBejegyzések= tktext.ScrolledText( frm, width= 50, wrap= tk.CHAR, state="disabled")

#--- Callbacks

def kiválasztás( event):

    """
    if event:
        index= event.widget.current()
        print( db.Tagok[ index] )
    """

    név1= db.Tagok[ cboxNevek1.current() ]
    név2= db.Tagok[ cboxNevek2.current() ]
    ltext= []

    if név1 != név2:
        for besz in db.Csevegések:
            if név1 == besz.név1 and név2 == besz.név2:
                ltext.append( f"{len(ltext)+1}. {db.dt2str(besz.tkezd)} --> {db.dt2str(besz.tbef)}" )

    if not ltext:
        ltext.append( "Nem történt beszélgetés." )

    textBejegyzések["state"]= "normal"
    textBejegyzések.delete( "1.0", "end")
    textBejegyzések.insert( "1.0", "\n".join(ltext) )
    textBejegyzések["state"]= "disabled"


cboxNevek1.bind('<<ComboboxSelected>>', kiválasztás)
cboxNevek2.bind('<<ComboboxSelected>>', kiválasztás)

#--- Geometry
lblKezdeményező.grid( row=0, column=0, sticky= tk.W)
cboxNevek1.grid( row=0, column= 1, sticky= tk.W)

lblFogadó.grid( row=1, column=0, sticky= tk.W)
cboxNevek2.grid( row=1, column= 1, sticky= tk.W)

lblCsevegések.grid( row=2, column=0, sticky=tk.W, pady=5 )
textBejegyzések.grid( row=3, column=0, columnspan= 2)

frm.grid( padx=15, pady=15)

kiválasztás( None)
#---
win.mainloop()

#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben