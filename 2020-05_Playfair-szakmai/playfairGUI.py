#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# playfairGUI.py
# ÁGAZATI érettségi feladat: 2020. május, Playfair-négyzet, GUI
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2020

# Egy dokumentáció a Tkinterhez: https://tkdocs.com/tutorial

import playfair # importáljuk a CLI-s programot
import tkinter as tk
import tkinter.scrolledtext as tktext


class PlayfairFrame(tk.Frame):

    def __init__(self, parent, fkeytable, finitial_text):

        super().__init__(parent)

        with open(finitial_text) as ff:
            itxt= ff.read()

        self.lbl= tk.Label(text="Előkészített szöveg", fg="green")
        self.lbl.grid(row=0, column=0, sticky=tk.W)

        self.tbox1= tktext.ScrolledText(self, height=5, wrap=tk.CHAR)
        self.tbox1.insert("1.0", itxt)
        self.tbox1.grid(row=1, column=0)

        self.tbox2= tktext.ScrolledText(self, height=5, wrap=tk.CHAR, state="disabled")
        self.tbox2.grid(row=2, column=0)

        self.tbox1.bind("<<Modified>>", self.check_text)

        self.pfair= playfair.PlayfairKódoló(fkeytable)


    def check_text(self,event):

        #print(event.widget is self.tbox1)
        self.tbox1.edit_modified(False)
        color= "green"
        words= self.tbox1.get("1.0","end").replace("\n"," ").strip().split(" ")
        for w in words:

            if len(w) != 2:
                color= "red"
                break
            if not self.pfair.Index(w[0]) or not self.pfair.Index(w[1]):
                color= "blue"
                break

        else:
            for w in words:
                if w[0]==w[1]:
                    color= "magenta"
                    break

        self.lbl.config(fg=color)

        if color in ("green","magenta"):

            self.tbox2.config(state="normal")
            self.tbox2.delete("1.0","end")
            self.tbox2.insert( "1.0", " ".join([ self.pfair.KódolBetűpár(w) for w in words ]) )
            self.tbox2.config(state="disabled")


#----------------------
win= tk.Tk()
win.title("playfairGUI")

pf= PlayfairFrame(win, "kulcstabla.txt", "szoveg.txt")
pf.grid()

win.mainloop()

#---------------------------------------------------------------------------
# További feladatok: https://eutlantis.k2os.hu
# Ajánlott könyv:    Koós Antal: Python a gépben
