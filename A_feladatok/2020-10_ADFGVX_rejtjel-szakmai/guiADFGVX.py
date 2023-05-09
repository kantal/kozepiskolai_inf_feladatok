#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# guiADFGVX.py
# ÁGAZATI érettségi feladat: 2020. október, ADFGVX-rejtjelezés, GUI
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2020

""" A feladatot a kiírás szerint Java vagy C# nyelven kellett megoldani,
    de mi most gyakorlásképpen Pythonban készítjük el.
"""
import tkinter as tk
import tkinter.scrolledtext as tktext
import tkinter.filedialog as tkfdlg
import string

class ADFGVXFrame(tk.Frame):

    def __init__(self, parent):

        super().__init__(parent)

        self.codetable= None

        self.lbl1= tk.Label(self,text="Az ellenőrzés eredménye:")
        self.btn= tk.Button(self,text="Kódtábla betöltése", command=self.betölt)
        self.tbox1= tktext.ScrolledText(self, height=16, width=40, state="disabled")
        self.lbl2= tk.Label(self,text="A betöltött kódtábla:")
        self.tbox2= tktext.ScrolledText(self, height=6, width=12, state="disabled")

        self.lbl1.grid(row=0, column=0, pady=5)
        self.btn.grid(row=0, column=2, pady=5)
        self.tbox1.grid(row=1, column=0, columnspan=3, pady=5)
        self.lbl2.grid(row=2, column=0, pady=5)
        self.tbox2.grid(row=3, column=1, pady=5)
        self.grid()


    def betölt(self):

        fname= tkfdlg.askopenfilename(title="Kódtábla választása", \
                 filetypes= [("kódtábla","k[óo]dt[áa]bla*.txt"),("kódtábla","*.ktbl")] )

        if fname:
            with open(fname) as ff:
                self.codetable= [ row.strip() for row in ff ]

            self.tbox2.config(state="normal")
            self.tbox2.delete("1.0","end")

            for row in self.codetable:
                self.tbox2.insert( "end", " ".join(list(row))+"\n" )

            self.tbox2.config(state="disabled")

            self.ellenőrzés()


    def ellenőrzés(self):

        vchars= string.ascii_lowercase + string.digits
        chars= "".join(self.codetable)

        valid= True

        if self.codetable:

            self.tbox1.config(state="normal")
            self.tbox1.delete("1.0","end")

            if len(self.codetable) != 6  or  any(len(row)!=6 for row in self.codetable):
                self.tbox1.insert("end", "Hiba a mátrix méretében!\n")
                valid= False

            for k in chars:
                if k not in vchars:
                    self.tbox1.insert("end", f"Hibás karakter ({k}) van a mátrixban!\n")
                    valid= False

            for k in vchars:
                cnt= chars.count(k)
                if cnt!=1:
                    self.tbox1.insert("end", f"A(z) {k} karakter {cnt}x szerepel a mátrixban!\n")
                    valid= False

            if valid:
                self.tbox1.insert("end","A mátrix megfelelő.\n")

            self.tbox1.config(state="disabled")

#--
win= tk.Tk()
win.option_add("*TkFDialog*foreground","black")
win.option_add("*TkFDialog*background","lightgray")
win.title("ADFGVX gui")
win.resizable(False,False)

AF= ADFGVXFrame(win)

win.mainloop()

#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben
