#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# Pars2012GUI.py
# ÁGAZATI érettségi feladat: 2021. május, Kalapácsvetés, GUI
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2022

""" A feladatot a kiírás szerint Java vagy C# nyelven kellett megoldani,
    de mi most gyakorlásképpen Pythonban készítjük el.
"""

import tkinter as tk
from tkinter import ttk

# A Pillow modul telepítése:
# Windowson: python -m pip install Pillow
# Linuxon: sudo apt-get install python3-pil
from PIL import ImageTk, Image

from Pars2012 import Versenyző


f_selejtező= "Selejtezo2012.txt"

with open( f_selejtező) as ff:

    next(ff)
    versenyzők= [ Versenyző(s) for s in ff ]

versenyzők.sort( key= lambda v: v.Eredmény, reverse= True)


win= tk.Tk()
win.title( "London 2012 – Férfi kalapácsvetés – selejtező")

frm= ttk.Frame( win)
lbl1= ttk.Label( frm, text="Válasszon versenyzőt!")

cbox= ttk.Combobox( frm)
tkv_név= tk.StringVar( )
cbox[ "textvariable"]= tkv_név
cbox[ "values"]= [ v.Név for v in versenyzők ]
cbox[ "state"]= ["readonly"]
cbox.current(0)

lbl_csoport= ttk.Label( frm)
lbl_nemzet= ttk.Label( frm)
lbl_kód= ttk.Label( frm)
lbl_sorozat= ttk.Label( frm)
lbl_eredmény= ttk.Label( frm)
lbl_zászló= ttk.Label( frm, text= "Zászló:")
lbl_zászlókép= ttk.Label( frm)

kép= None

def cbox_callback( event):
    global kép

    index= cbox.current()
    v= versenyzők[ index]

    lbl_csoport["text"]=  f"Csoport: {v.Csoport}"
    lbl_nemzet["text"]= f"Nemzet: {v.Nemzet}"
    lbl_kód["text"]= f"Nemzet kód: {v.Kód}"

    sorozat= ";".join( v.s_dobások)
    lbl_sorozat["text"]= f"Sorozat: {sorozat}"

    eredmény= str(v.Eredmény).replace(".",",")
    lbl_eredmény["text"]= f"Eredmény: {eredmény}"

    f_img= f"Images/{v.Kód}.png"
    kép= ImageTk.PhotoImage( Image.open( f_img))
    lbl_zászlókép["image"]= kép


cbox.bind( "<<ComboboxSelected>>", cbox_callback)

lbl1.grid( row= 0, column= 0)
cbox.grid( row= 1, column= 0)
cbox["width"]= max( len(v.Név) for v in versenyzők )

lbl_csoport.grid( row= 2, column= 0, sticky= tk.W )
lbl_csoport.grid( row= 3, column= 0, sticky= tk.W)
lbl_nemzet.grid( row= 4, column= 0, sticky= tk.W)
lbl_kód.grid( row= 5, column= 0, sticky= tk.W)
lbl_sorozat.grid( row= 6, column= 0, sticky= tk.W)
lbl_eredmény.grid( row= 7, column= 0, sticky= tk.W)
lbl_zászló.grid( row= 8, column= 0, sticky= tk.W)
lbl_zászlókép.grid( row= 9, column= 0, sticky= tk.W+tk.N+tk.E+tk.S)

frm["pad"]= 15
frm.grid()

cbox_callback( None)

win.mainloop()

#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben
