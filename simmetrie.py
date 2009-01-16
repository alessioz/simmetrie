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

# versione 0.2
# 29 gennaio 2007

import Image, ImageOps, ImageTk
import Tkinter
import tkFileDialog

class Gui:
	def __init__(self):
		self.root = Tkinter.Tk()
		self.root.title("Simmetrie 0.2")

		self.menu = Tkinter.Menu(self.root)
		self.root.config(menu=self.menu)
		self.menu.config(borderwidth=1)
		self.crea_menu_file()
		self.crea_menu_info()
		self.crea_canvas_immagine()
		self.image = Image.open("logo.jpg")
		self.dimensioni_video()
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
		
	def crea_menu_info(self):
		self.infoMenu = Tkinter.Menu(self.menu, tearoff=0)
		self.menu.add_cascade(label="Info", menu=self.infoMenu)
		self.infoMenu.add_command(label="Info", command=self.info)
		
	def dimensioni_video(self):
		self.larg_schermo = self.root.winfo_screenwidth()
		self.alt_schermo = self.root.winfo_screenheight()
		print self.larg_schermo, self.alt_schermo
		
	def apri_immagine(self):	
		
		self.file = tkFileDialog.askopenfilename(filetypes=[("Immagini JPG", (".jpg", ".jpeg", ".JPG")),("Tutti i file","*")])
		if self.file:
			self.image = Image.open(self.file)					
			self.dimensioni = self.image.size
			print self.dimensioni[0]
			new_larg=self.dimensioni[1]*self.larg_schermo/3/self.dimensioni[0]
			print new_larg
			if self.dimensioni[0] > self.larg_schermo/3:
				print "si"
				self.image = self.image.resize((self.larg_schermo/3, new_larg))
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
			
	def info(self):
		self.about = Tkinter.Toplevel(self.root)
		self.about.config(borderwidth=10)
		self.about.title("Simmetrie")
		self.h = Tkinter.Label(self.about, text="Simmetrie 0.2", font=("Helvetica", 16), borderwidth=10)
		self.i = Tkinter.Label(self.about, text="This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 2 of the License, or (at your option) any later version.", borderwidth=5, wraplength=200);
		self.k = Tkinter.Label(self.about, text="Copyright (c) Alessio Zanol\nnardei@infinito.it")
		self.l = Tkinter.Button(self.about, text="OK", command=self.about.destroy)
		self.h.pack()
		self.i.pack()
		self.k.pack()
		self.l.pack()
		self.root.wait_windowself(self.about)

			
		
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
		self.canvas.config(width=self.photo.width(), height=self.photo.height(), cursor="center_ptr")
		self.canvas.pack(side="left")
	
	def mostra_immagine_originale(self):
		self.dimensioni = self.image.size
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
		nuovaimmaginesx.save("partesx.jpg")
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
		nuovaimmaginedx.save("partedx.jpg")
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