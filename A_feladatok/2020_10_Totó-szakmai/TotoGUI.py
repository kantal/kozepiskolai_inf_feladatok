#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# TotoGUI.py
# ÁGAZATI érettségi feladat: 2020. október, Totó, GUI
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2020

""" A feladatot a kiírás szerint Java vagy C# nyelven kellett megoldani,
    de mi most gyakorlásképpen Pythonban készítjük el a Tkinter modul használatával.
"""
import tkinter as tk

class FordulóEllenőrzőFrame(tk.Frame):

    def __init__(self,parent):

        super().__init__(parent)

        self.lbl= tk.Label(self,text="Kérem a forduló eredményeit [1,2,X]:")

        self.svar_forduló= tk.StringVar()
        itext= "12X12X12X12X12"
        self.svar_forduló.set(itext)
        self.entry= tk.Entry(self, textvariable=self.svar_forduló)
        self.entry["validate"]="all"
        self.entry["validatecommand"]= (self.register(self.check), '%P')

        self.ivar_count= tk.IntVar()
        self.svar_count= tk.StringVar()
        self.svar_count_def= "Nem megfelelő a karakterek száma"
        self.btn_count= tk.Checkbutton(self, variable=self.ivar_count, \
                                        textvariable=self.svar_count, \
                                        state="disabled")
        self.btn_count["disabledforeground"]= self.btn_count.cget("foreground")

        self.ivar_invchar= tk.IntVar()
        self.svar_invchar= tk.StringVar()
        self.svar_invchar_def= "Helytelen karakter az eredményekben"
        self.btn_invchar= tk.Checkbutton(self, textvariable=self.svar_invchar, \
                                        variable=self.ivar_invchar, \
                                        state="disabled")
        self.btn_invchar["disabledforeground"]= self.btn_invchar.cget("foreground")

        self.btn_save= tk.Button(self,text="Eredmények mentése", command=lambda: print("Gombnyomás"))

        self.check(itext)

        self.lbl.grid(row=0,column=0, sticky=tk.W)
        self.entry.grid(row=1,column=0, sticky=tk.W)
        self.btn_count.grid(row=2,column=0, sticky=tk.W)
        self.btn_invchar.grid(row=3,column=0, sticky=tk.W)
        self.btn_save.grid(row=4,column=0, sticky=tk.W)

        parent.rowconfigure(0,pad=15)
        parent.columnconfigure(0,pad=15)
        self.grid()


    def check(self,txt):

        self.btn_count["state"]="normal"
        self.btn_invchar["state"]="normal"

        self.ivar_count.set( 1 if len(txt)!=14 else 0 )
        self.svar_count.set( f"{self.svar_count_def} ({len(txt)})" )

        l= [k for k in txt if k not in "12X"]
        self.ivar_invchar.set( 1 if l else 0 )
        self.svar_invchar.set(self.svar_invchar_def if not l else self.svar_invchar_def+"(" + ";".join(l) + ")")

        self.btn_count["state"]="disabled"
        self.btn_invchar["state"]="disabled"
        self.btn_save["state"]= "disabled" if len(txt)!= 14 or l else "normal"

        return True

#--
win= tk.Tk()
win.title("Totóeredmény-ellenőrző")
win.resizable(False,False)

E= FordulóEllenőrzőFrame(win)

win.mainloop()

#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben
