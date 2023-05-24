import tkinter as tk
from PIL import Image, ImageTk 

#crear ventana
ventana=tk.Tk()
ventana.title("Tarea de cambio de imagenes")
ventana.geometry("800x800")

# primera imagen
i1 = Image.open('C:/Users/berna/OneDrive/Imágenes/pokemon odish/depositphotos_120226152-stock-illustration-pokemon-go-pokeball-round-sign.jpg')
i1=i1.resize((250,250))
imagen1= ImageTk.PhotoImage(i1)

Imagen1 = tk.Label(ventana, image=imagen1)
Imagen1.grid(columnspan=4, row=0, column=0)

#segunda
i2 = Image.open('C:/Users/berna/OneDrive/Imágenes/pokemon odish/depositphotos_120226152-stock-illustration-pokemon-go-pokeball-round-sign.jpg')
i2=i2.resize((250,250))
imagen2= ImageTk.PhotoImage(i2)

Imagen2 = tk.Label(ventana, image=imagen2)
Imagen2.grid(columnspan=4,row=0, column=4)

#tercera


i3= Image.open('C:/Users/berna/OneDrive/Imágenes/pokemon odish/depositphotos_120226152-stock-illustration-pokemon-go-pokeball-round-sign.jpg')
i3=i3.resize((250,250))
imagen3=ImageTk.PhotoImage(i3)
Eti3=tk.Label(ventana, image=imagen3)
Eti3.grid(columnspan=4,row=2, column=0)




#cuarta
i4 = Image.open('C:/Users/berna/OneDrive/Imágenes/pokemon odish/depositphotos_120226152-stock-illustration-pokemon-go-pokeball-round-sign.jpg')
i4=i4.resize((250,250))
imagen4= ImageTk.PhotoImage(i4)

Imagen4 = tk.Label(ventana, image=imagen4)
Imagen4.grid(columnspan=4,row=2, column=4)

###############################################################################################################

#CambioI1
Cambio1=Image.open('C:/Users/berna/OneDrive/Imágenes/pokemon odish/5UQQSEMDT5FM5JOWITUXQFW3OQ-1.jpg')
Cambio1 = Cambio1.resize((250,250))
CambioTk1 = ImageTk.PhotoImage(Cambio1)
def cambiarImagen1():
    Imagen1.config(image= CambioTk1)
botonCambio1 = tk.Button(ventana, text="Odish", command = cambiarImagen1)
botonCambio1.grid(row=1, column=0)
#CambioI12
Cambio2=Image.open('C:/Users/berna/OneDrive/Imágenes/pokemon odish/5UQQSEMDT5FM5JOWITUXQFW3OQ-2.jpg')
Cambio2 = Cambio2.resize((250,250))
CambioTk2 = ImageTk.PhotoImage(Cambio2)
def cambiarImagen2():
    Imagen1.config(image= CambioTk2)
botonCambio2 = tk.Button(ventana, text="Gloom", command = cambiarImagen2)
botonCambio2.grid(row=1, column=1)
#Cambio13
Cambio3=Image.open('C:/Users/berna/OneDrive/Imágenes/pokemon odish/5UQQSEMDT5FM5JOWITUXQFW3OQ-3.jpg')
Cambio3 = Cambio3.resize((250,250))
CambioTk3 = ImageTk.PhotoImage(Cambio3)
def cambiarImagen3():
    Imagen1.config(image= CambioTk3)
botonCambio3 = tk.Button(ventana, text="Bellosom", command = cambiarImagen3)
botonCambio3.grid(row=1, column=2)
#CambioI14
Cambio4=Image.open('C:/Users/berna/OneDrive/Imágenes/pokemon odish/depositphotos_120226152-stock-illustration-pokemon-go-pokeball-round-sign.jpg')
Cambio4 = Cambio4.resize((250,250))
CambioTk4 = ImageTk.PhotoImage(Cambio4)
def cambiarImagen4():
    Imagen1.config(image= CambioTk4)
botonCambio4 = tk.Button(ventana, text="Pokeball", command = cambiarImagen4)
botonCambio4.grid(row=1, column=3)
#CambiarImagen2
Cambio5=Image.open('C:/Users/berna/OneDrive/Imágenes/pokemon odish/1658398390_archive_2016121314208_1_rz500-1.jpg')
Cambio5 = Cambio5.resize((250,250))
CambioTk5 = ImageTk.PhotoImage(Cambio5)
def cambiarImagen5():
    Imagen2.config(image= CambioTk5)
botonCambio5 = tk.Button(ventana, text="Chikorita", command = cambiarImagen5)
botonCambio5.grid(row=1, column=4)

Cambio6=Image.open('C:/Users/berna/OneDrive/Imágenes/pokemon odish/1658398390_archive_2016121314208_1_rz500-2.jpg')
Cambio6 = Cambio6.resize((250,250))
CambioTk6 = ImageTk.PhotoImage(Cambio6)
def cambiarImagen6():
    Imagen2.config(image= CambioTk6)
botonCambio6 = tk.Button(ventana, text="Bayleef", command = cambiarImagen6)
botonCambio6.grid(row=1, column=5)

Cambio7=Image.open('C:/Users/berna/OneDrive/Imágenes/pokemon odish/1658398390_archive_2016121314208_1_rz500-3.jpg')
Cambio7 = Cambio7.resize((250,250))
CambioTk7 = ImageTk.PhotoImage(Cambio7)
def cambiarImagen7():
    Imagen2.config(image= CambioTk7)
botonCambio7 = tk.Button(ventana, text="Meganium", command = cambiarImagen7)
botonCambio7.grid(row=1, column=6)

Cambio8=Image.open('C:/Users/berna/OneDrive/Imágenes/pokemon odish/depositphotos_120226152-stock-illustration-pokemon-go-pokeball-round-sign.jpg')
Cambio8 = Cambio8.resize((250,250))
CambioTk8 = ImageTk.PhotoImage(Cambio8)
def cambiarImagen8():
    Imagen2.config(image= CambioTk8)
botonCambio8 = tk.Button(ventana, text="Pokeball", command = cambiarImagen8)
botonCambio8.grid(row=1, column=7)
#CambiarImagen3
Cambio9=Image.open('C:/Users/berna/OneDrive/Imágenes/pokemon odish/1658398390_archive_2016121314208_1_rz500-21.jpg')
Cambio9 = Cambio9.resize((250,250))
CambioTk9 = ImageTk.PhotoImage(Cambio9)
def cambiarImagen9():
    Eti3.config(image= CambioTk9)
botonCambio9 = tk.Button(ventana, text="Cyndaquil", command = cambiarImagen9)
botonCambio9.grid(row=3, column=0)

Cambio10=Image.open('C:/Users/berna/OneDrive/Imágenes/pokemon odish/1658398390_archive_2016121314208_1_rz500-22.jpg')
Cambio10 = Cambio10.resize((250,250))
CambioTk10 = ImageTk.PhotoImage(Cambio10)
def cambiarImagen10():
   Eti3.config(image= CambioTk10)
botonCambio10 = tk.Button(ventana, text="Quilava", command = cambiarImagen10)
botonCambio10.grid(row=3 ,column=1)

Cambio11=Image.open('C:/Users/berna/OneDrive/Imágenes/pokemon odish/1658398390_archive_2016121314208_1_rz500-23.jpg')
Cambio11 = Cambio11.resize((250,250))
CambioTk11 = ImageTk.PhotoImage(Cambio11)
def cambiarImagen11():
   Eti3.config(image= CambioTk11)
botonCambio11 = tk.Button(ventana, text="Typhlosion", command = cambiarImagen11)
botonCambio11.grid(row=3, column=2)

Cambio12=Image.open('C:/Users/berna/OneDrive/Imágenes/pokemon odish/depositphotos_120226152-stock-illustration-pokemon-go-pokeball-round-sign.jpg')
Cambio12 = Cambio12.resize((250,250))
CambioTk12 = ImageTk.PhotoImage(Cambio12)
def cambiarImagen12():
   Eti3.config(image= CambioTk12)
botonCambio12 = tk.Button(ventana, text="Pokeball", command = cambiarImagen12)
botonCambio12.grid(row=3, column=3)
#Cambiar cuarta imagen
Cambio13=Image.open('C:/Users/berna/OneDrive/Imágenes/pokemon odish/1658398390_archive_2016121314208_1_rz500-31.jpg')
Cambio13 = Cambio13.resize((250,250))
CambioTk13 = ImageTk.PhotoImage(Cambio13)
def cambiarImagen13():
    Imagen4.config(image= CambioTk13)
botonCambio13 = tk.Button(ventana, text="Totodile", command = cambiarImagen13)
botonCambio13.grid(row=3, column=4)

Cambio14=Image.open('C:/Users/berna/OneDrive/Imágenes/pokemon odish/1658398390_archive_2016121314208_1_rz500-32.jpg')
Cambio14 = Cambio14.resize((250,250))
CambioTk14 = ImageTk.PhotoImage(Cambio14)
def cambiarImagen14():
    Imagen4.config(image= CambioTk14)
botonCambio14 = tk.Button(ventana, text="Croconaw", command = cambiarImagen14)
botonCambio14.grid(row=3, column=5)

Cambio15=Image.open('C:/Users/berna/OneDrive/Imágenes/pokemon odish/1658398390_archive_2016121314208_1_rz500-33.jpg')
Cambio15 = Cambio15.resize((250,250))
CambioTk15 = ImageTk.PhotoImage(Cambio15)
def cambiarImagen15():
    Imagen4.config(image= CambioTk15)
botonCambio15 = tk.Button(ventana, text="Feraligatr", command = cambiarImagen15)
botonCambio15.grid(row=3, column=6)

Cambio16=Image.open('C:/Users/berna/OneDrive/Imágenes/pokemon odish/depositphotos_120226152-stock-illustration-pokemon-go-pokeball-round-sign.jpg')
Cambio16 = Cambio16.resize((250,250))
CambioTk16 = ImageTk.PhotoImage(Cambio16)
def cambiarImagen16():
    Imagen4.config(image= CambioTk16)
botonCambio16 = tk.Button(ventana, text="Pokeball", command = cambiarImagen16)
botonCambio16.grid(row=3, column=7)

ventana.mainloop()

