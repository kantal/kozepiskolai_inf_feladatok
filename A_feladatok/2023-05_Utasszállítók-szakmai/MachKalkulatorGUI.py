#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# MachKalkulatorGUI.py
# Szakmai érettségi feladat: 2023. május, Utasszállítók, GUI
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2023

""" A feladatot a kiírás szerint Java vagy C# nyelven kellett megoldani,
    de mi most gyakorlásképpen Pythonban készítjük el.
"""

import tkinter as tk
from tkinter import ttk
import tkinter.scrolledtext as tktext
import tkinter.messagebox as tkmsg
import math

#--- Widgets
win= tk.Tk()
win.title( "Mach-szám kalkulátor")
win.resizable( width=False, height=False)

frm= ttk.Frame( win, border=10)
lblTny= ttk.Label( frm, text= "Torlónyomás:")
lblSny= ttk.Label( frm, text= "Statikus nyomás:")
btnSzámol= ttk.Button( frm, text= "Számol")

tkvTny= tk.StringVar()
tkvSny= tk.StringVar()
entryTny= ttk.Entry( frm, textvariable= tkvTny )
entrySny= ttk.Entry( frm, textvariable= tkvSny )

lblEredmények= ttk.Label( frm, text= "Eredmények:")
textBejegyzések= tktext.ScrolledText( frm, wrap= tk.CHAR, state="disabled")

#--- Logic
def Számol():

    try:
        qc= float( tkvTny.get().replace(",",".") )
        p0= float( tkvSny.get().replace(",",".") )
    except ValueError:
        tkmsg.showerror( title="MachKalkulátor hiba", message= "Az input nem értelmezhető számként!")
        return

    Ma= math.sqrt( 5 * ( math.pow( qc/p0 +1, 2/7) -1) )

    textBejegyzések["state"]= "normal"
    if Ma < 1:
        textBejegyzések.insert( "end", f"qc={qc} p0={p0} Ma={Ma}\n")
    else:
        textBejegyzések.insert( "end", "(1.0-t elérő/meghaladó érték)\n" )
    textBejegyzések["state"]= "disabled"


btnSzámol["command"]= Számol

#--- Layout
lblTny.grid( row=0, column=0, sticky= tk.W, pady=5 )
lblSny.grid( row=1, column=0, sticky= tk.W, pady=5 )
entryTny.grid( row=0, column=1, sticky= tk.W )
entrySny.grid( row=1, column=1, sticky= tk.W )
btnSzámol.grid( row=0, column=2, rowspan=2, sticky= tk.W+tk.E+tk.N+tk.S)
lblEredmények.grid( row=2, column=0, sticky= tk.W, pady=5 )
textBejegyzések.grid( row=3, column=0, columnspan=3 )
frm.grid()

#---
win.mainloop()


#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben
