#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# BukkMaraton2019GUI.py
# Szakmai érettségi feladat: 2022. október, Hegyikerékpár, GUI
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2023

""" A feladatot a kiírás szerint Java vagy C# nyelven kellett megoldani,
    de mi most gyakorlásképpen Pythonban készítjük el.
"""

import tkinter as tk
from tkinter import ttk

#--- Data
Távok= [ ("Mini",16), ("Rövid", 38), ("Pedelec", 54), ("Közép", 57), ("Hosszú", 94) ]

#--- Widgets
win= tk.Tk()
win.title( "BukkMaraton2019GUI")
win.resizable( width=False, height=False)

frm= ttk.Frame( win)

lblTáv= ttk.Label( frm, text="Táv:")
cboxTáv= ttk.Combobox( frm, values= [ f"{táv_neve} - {hossza}km" for táv_neve,hossza in Távok ], state= "readonly", width= 20 )
cboxTáv.current(3)

btnSzámol= ttk.Button( frm, text= "Számol")

lblIdő= ttk.Label( frm, text= "Idő [óra:perc:mp]:")
tkvIdő= tk.StringVar()
tkvIdő.set( "1:00:00")
entryIdő= ttk.Entry( frm, textvariable= tkvIdő, width= 9)

sKmh= "Átlagsebesség [km/h]:"
sMs=  "Átlagsebesség [m/s]:"
lblKmh= ttk.Label( frm, text= sKmh)
lblMs= ttk.Label( frm, text= sMs )

#--- Callback
def számol():

    táv= Távok[ cboxTáv.current() ][1] * 1000
    try:
        óra, perc, mp= [ int(t) for t in tkvIdő.get().split(":") ]
        ms=  táv / (óra*3600 + perc*60 + mp)
        kmh= ms* 3.6
    except ValueError:
        ms= kmh= 0

    lblMs["text"]= f"{sMs} {ms:.2f}"
    lblKmh["text"]= f"{sKmh} {kmh:.2f}"

btnSzámol["command"]= számol

#--- Layout
lblTáv.grid( row= 0, column= 0, padx= 5, sticky= tk.W)
cboxTáv.grid( row= 0, column= 1, padx= 5)

btnSzámol.grid( row=0, column= 2, rowspan= 2, padx= 5, sticky= tk.W+tk.E+tk.N+tk.S )

lblIdő.grid( row=1, column=0, padx= 5, sticky= tk.W)
entryIdő.grid( row=1, column=1, pady= 5)

lblKmh.grid( row=2, column=0, columnspan=2, padx=5, sticky= tk.W)
lblMs.grid( row=3, column=0, columnspan=2, padx=5, sticky= tk.W)

frm.grid( padx=15, pady=15)

#---
win.mainloop()



#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben