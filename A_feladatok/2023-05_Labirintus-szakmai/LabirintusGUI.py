#!/usr/bin/env python3
# LabirintusGUI.py
# Szakmai érettségi feladat: 2023. május, Labirintus, GUI
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2023

""" A feladatot a kiírás szerint Java vagy C# nyelven kellett megoldani,
    de mi most gyakorlásképpen Pythonban készítjük el.
"""

import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as tkmsg
import sys      # sys.exc_info()

#--- WIDGETS ---

win= tk.Tk()
win.title( "Labirintuskészítő")
win.resizable( width= False, height= False)

frmMain= ttk.Frame( win)
lblMéret= ttk.Label( frmMain, text= "Labirintus mérete [sor x oszlop]" )

rng_sor= range(5,21)
rng_oszlop= range(5,21)
cboxSor= ttk.Combobox( frmMain, values= list( rng_sor), state="readonly", width= 3 )
cboxOszlop= ttk.Combobox( frmMain, values= list( rng_oszlop), state="readonly", width= 3 )
cboxSor.current( rng_sor.index(12) )
cboxOszlop.current( rng_oszlop.index(12) )

btnInduló= ttk.Button( frmMain, text= "Induló labirintus létrehozása")
btnMentés= ttk.Button( frmMain, text= "Labirintus mentése")
rng_sorszám= range(1,17)
cboxSorszám= ttk.Combobox( frmMain, values= list(rng_sorszám), width= 3 )
cboxSorszám.current( rng_sorszám.index(3) )

frmCellák= None
cellák= None


def cellaRács( n_sor, n_oszlop):
    global frmCellák, cellák

    if frmCellák:
        frmCellák.destroy()

    frmCellák= ttk.Frame( frmMain)
    cellák=[]
    for sor in range( n_sor):

        cella_sor= []
        for oszlop in range( n_oszlop):

            cella= ttk.Button( frmCellák, text= " ", width= 1)

            if sor == 0 or sor == n_sor-1 or oszlop == 0 or oszlop == n_oszlop-1:

                cella["state"]= "disabled"
                cella["text"]= "X"
            else:
                cella.bind( "<ButtonPress-1>", cellaVáltó)

            cella_sor.append( cella)

        cellák.append( cella_sor)

    cellák[1][0]["text"] = cellák[n_sor-2][n_oszlop-1]["text"] = " "



#--- LOGIC ---

def labKészítő():
    global frmCellák, cellák

    n_sor= rng_sor[ cboxSor.current() ]
    n_oszlop= rng_oszlop[ cboxOszlop.current() ]

    cellaRács( n_sor, n_oszlop)
    cellaElrendezés( n_sor, n_oszlop)


def cellaVáltó( event):

    w= event.widget
    if w["text"] == " ":
        w.configure( text = "X")
    else:
        w.configure( text = " ")


def Mentés():

    msg_title= "Labirintuskészítő"

    if not cellák:
        tkmsg.showerror( title= msg_title, message="Nincs mit elmenteni!")
        return

    sorszám= cboxSorszám["values"][ cboxSorszám.current()]
    fn= f"Lab{sorszám}.txt"

    msg_error= "Az állomány mentése nem sikerült!"

    try:
        with open( fn, "w") as ff:

            for sor in cellák:
                s_sor= "".join( [ cell["text"] for cell in sor ] )
                ff.write( f"{s_sor}\n")

    except (OSError, PermissionError) as esemény:
        tkmsg.showerror( title= msg_title, message= f"{msg_error}\n{esemény}")
    except: # egyéb esemény:
        #tkmsg.showerror( title= msg_title, message= f"{msg_error}\nValami bibi van!")
        tkmsg.showerror( title= msg_title, message= f"{msg_error}\n{sys.exc_info()}")
    else:
        tkmsg.showinfo( title= msg_title, message= f"Az állomány mentése sikeres!\n{fn}")


btnInduló[ "command"]= labKészítő
btnMentés[ "command"]= Mentés

#--- LAYOUT ---

lblMéret.grid( row= 0, column= 0, sticky= tk.W, pady= 5)

cboxSor.grid( row= 0, column= 1, pady= 5, sticky= tk.E)
cboxOszlop.grid( row= 0, column= 2, pady= 5, sticky= tk.W)

btnInduló.grid( row= 1, column= 0, pady= 5)
btnMentés.grid( row= 1, column= 1, pady= 5)
cboxSorszám.grid( row= 1, column= 2, pady= 5)


def cellaElrendezés( n_sor, n_oszlop):
    global frmCellák, cellák

    for sor in range( n_sor):
        for oszlop in range( n_oszlop):
            cellák[sor][oszlop].grid( row= sor, column= oszlop )

    frmCellák.grid( row= 2, column= 0, columnspan= 3)


frmMain.grid( padx= 5, pady= 5)

#---
win.mainloop()


#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben
