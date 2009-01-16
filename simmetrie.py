#!/usr/bin/env python
"""
    Copyright (C) 2007 Alessio Zanol <nardei@infinito.it>
     
    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program; if not, write to the Free Software
    Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
"""

# versione 0.1
# 29 dicembre 2007

import Image, ImageOps, ImageTk
import Tkinter

class Gui:
        def __init__(self):
                self.root = Tkinter.Tk()
                self.root.title("Simmetrie 0.1")

                self.menu = Tkinter.Menu(self.root)
                self.root.config(menu=self.menu)
                self.menu.config(borderwidth=1)
                self.crea_menu_file()
                self.crea_canvas_immagine()
                self.image = Image.open("logoMTSN.jpg")
                self.mostra_immagine_iniziale()
                self.root.mainloop()    
        

        def crea_menu_file(self):
                self.fileMenu = Tkinter.Menu(self.menu, tearoff=0)
                self.menu.add_cascade(label="File", menu=self.fileMenu)
                self.fileMenu.add_command(label="Apri Immagine", command=self.apri_immagine)
                self.fileMenu.add_command(label="Salva Immagine SINISTRA", command=self.salva_immagine_sinistra)
                self.fileMenu.add_command(label="Salva Immagine DESTRA", command=self.salva_immagine_destra)
                self.fileMenu.add_separator()
                self.fileMenu.add_command(label="Chiudi", command=self.root.quit)
                
                
        def apri_immagine(self):        
                import tkFileDialog
                self.file = tkFileDialog.askopenfilename(filetypes=[("Immagini JPG", (".jpg", ".jpeg")),("Tutti i file","*")])
                if self.file:
                        self.image = Image.open(self.file)
                        self.mostra_immagine_originale()
                        self.specchia()

        def salva_immagine_destra(self):
                import tkFileDialog
                self.salvafile = tkFileDialog.asksaveasfilename(filetypes=[("Immagini JPG", (".jpg", ".jpeg")),("Tutti i file","*")])
                if self.salvafile:
                        nuovaimmaginedx.save(self.salvafile+'.jpg')

        def salva_immagine_sinistra(self):
                import tkFileDialog
                self.salvafile = tkFileDialog.asksaveasfilename(filetypes=[("Immagini JPG", (".jpg", ".jpeg")),("Tutti i file","*")])
                if self.salvafile:
                        print self.salvafile
                        nuovaimmaginesx.save(self.salvafile+'.jpg')
                        
                
        def crea_canvas_immagine(self):
                self.canvas = Tkinter.Canvas(self.root)
                self.canvas.config(borderwidth=0)
                self.canvas2 = Tkinter.Canvas(self.root)
                self.canvas2.config(borderwidth=0)
                self.canvas3 = Tkinter.Canvas(self.root)
                self.canvas3.config(borderwidth=0)
                
        def mostra_immagine_iniziale(self):
                self.photo = ImageTk.PhotoImage(self.image)
                self.canvas.create_image(0,0, anchor="nw", image=self.photo)
                self.canvas.config(width=self.photo.width(),height=self.photo.height(), cursor="center_ptr")
                self.canvas.pack(side="left")
        
        def mostra_immagine_originale(self):            
                self.photo = ImageTk.PhotoImage(self.image)
                self.canvas.create_image(0,0, anchor="nw", image=self.photo)
                self.canvas.config(width=self.photo.width(),height=self.photo.height(), cursor="center_ptr")
                self.canvas.pack(side="left")
        
        def specchia(self):
                self.canvas.bind("<Button-1>", self.callback)
                
        def specchiatasx(self, boxsx, boxsxtraslato, lineaditaglio):
                imagecrop = self.imagesx.crop(boxsx)
                imagemirror = ImageOps.mirror(imagecrop)
                nuovaimmaginesx = Image.new("RGB",(lineaditaglio*2,self.dimensioni[1]))
                nuovaimmaginesx.paste(imagecrop, boxsx) 
                nuovaimmaginesx.paste(imagemirror, boxsxtraslato)
                global nuovaimmaginesx
                
                
                self.photo2 = ImageTk.PhotoImage(nuovaimmaginesx)
                self.canvas2.create_image(0,0, anchor="nw", image=self.photo2)
                self.canvas2.config(width=self.photo2.width(),height=self.photo2.height())
                self.canvas2.pack(side="left")



        def specchiatadx(self, boxdx, boxdxcrop, boxdxmirror, lineaditaglio):
                imagecrop = self.imagedx.crop(boxdx)
                imagemirror = ImageOps.mirror(imagecrop)
                nuovaimmaginedx = Image.new("RGB", ((self.dimensioni[0]-lineaditaglio)*2,self.dimensioni[1]))
                nuovaimmaginedx.paste(imagemirror, boxdxmirror)
                nuovaimmaginedx.paste(imagecrop, boxdxcrop)
                global nuovaimmaginedx
                
                self.photo3 = ImageTk.PhotoImage(nuovaimmaginedx)
                self.canvas3.create_image(0,0, anchor="nw", image=self.photo3)
                self.canvas3.config(width=self.photo3.width(),height=self.photo3.height())
                self.canvas3.pack(side="left")
                

        def callback(self, event):
                self.dimensioni = self.image.size
                self.imagesx = self.image.copy()
                self.imagedx = self.image.copy()
                
                self.lineaditaglio = event.x  #coordinata x
                self.boxsx = (0, 0, self.lineaditaglio, self.dimensioni[1])
                self.boxdx = (self.lineaditaglio, 0, self.dimensioni[0], self.dimensioni[1])
                self.boxsxtraslato = (self.lineaditaglio, 0, self.lineaditaglio*2, self.dimensioni[1])
        
                self.boxdxmirror = (0, 0, (self.dimensioni[0]-self.lineaditaglio), self.dimensioni[1])
                self.boxdxcrop = ((self.dimensioni[0]-self.lineaditaglio), 0, (self.dimensioni[0]-self.lineaditaglio)*2, self.dimensioni[1])
        
                self.specchiatasx(self.boxsx, self.boxsxtraslato, self.lineaditaglio)   
                self.specchiatadx(self.boxdx, self.boxdxcrop, self.boxdxmirror, self.lineaditaglio)

avvia = Gui()
