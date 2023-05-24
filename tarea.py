import tkinter as tk
from PIL import Image, ImageTk 

#crear ventana
ventana=tk.Tk()
ventana.title("Tarea de cambio de imagenes")
ventana.geometry("800x800")

#Label
etiqueta2 =tk.Label(ventana, text="Imagenes")
etiqueta2.grid(column=2,row=0)

#insert image
    # primera imagen
imagenSource2 = Image.open('C:/Users/berna/OneDrive/Imágenes/fondo/H2x1_Kirby30thAnniversary.jpg')
imagenSource2=imagenSource2.resize((300,300))
imagentk2= ImageTk.PhotoImage(imagenSource2)

etiquetaImagen2 = tk.Label(ventana, image=imagentk2)
etiquetaImagen2.grid(row=0, column=0, columnspan=4)



#segunda
imagenSource = Image.open('C:/Users/berna/OneDrive/Imágenes/god-of-war-pc-screenshot-03-en-12oct21.jpg')
imagenSource=imagenSource.resize((300,300))
imagentk= ImageTk.PhotoImage(imagenSource)

etiquetaImagen = tk.Label(ventana, image=imagentk)
etiquetaImagen.grid(row=1, column=2, columspan=4)



####################################



imagenCambio2=Image.open('C:/Users/berna/OneDrive/Imágenes/61fw7I5VRRL._AC_UF1000,1000_QL80_.jpg')
imagenCambio2 = imagenCambio2.resize((300,300))
imagenCambioTk1 = ImageTk.PhotoImage(imagenCambio2)
etiquetaImagen7 = tk.Label(ventana, image=imagentk2)
etiquetaImagen7.grid(row=1, column=1)

imagenCambio3=Image.open('C:/Users/berna/OneDrive/Imágenes/240.jpg')
imagenCambio3 = imagenCambio3.resize((300,300))
imagenCambioTk2 = ImageTk.PhotoImage(imagenCambio3)
etiquetaImagen8 = tk.Label(ventana, image=imagentk2)
etiquetaImagen8.grid(row=1, column=1)











#cambia la primer imagen

def cambiarImagen1():
    etiquetaImagen2.configure(image= imagenCambioTk1)
botonCambio1 = tk.Button(ventana, text="Cambiar1", command = cambiarImagen1)
botonCambio1.grid(row=0, column=1)

def cambiarImagen2():
    etiquetaImagen7.configure(image= imagenCambioTk2)
botonCambio11 = tk.Button(ventana, text="Cambiar2", command = cambiarImagen2)
botonCambio11.grid(row=1, column=1)

def cambiarImagen3():
    etiquetaImagen8.configure(image= imagenCambioTk3)
botonCambio3 = tk.Button(ventana, text="Cambiar3", command = cambiarImagen3)
botonCambio3.grid(row=1, column=2)

def cambiarImagen4():
    etiquetaImagen9.configure(image= imagenCambioTk)
botonCambio4 = tk.Button(ventana, text="Cambiar4", command = cambiarImagen4)
botonCambio4.grid(row=1, column=3)


#cambiar la segunda
imagenCambiosegunda=Image.open('C:/Users/berna/OneDrive/Imágenes/imagenes/DSC00383.JPG')
imagenCambiosegunda = imagenCambiosegunda.resize((300,300))
imagenCambioTk6 = ImageTk.PhotoImage(imagenCambiosegunda)
etiquetaImagen4 = tk.Label(ventana, image=imagentk)
etiquetaImagen4.grid(row=1, column=2)

imagenCambiosegunda=Image.open('C:/Users/berna/OneDrive/Imágenes/imagenes/DSC00383.JPG')
imagenCambiosegunda = imagenCambiosegunda.resize((300,300))
imagenCambioTk6 = ImageTk.PhotoImage(imagenCambiosegunda)
etiquetaImagen4 = tk.Label(ventana, image=imagentk)
etiquetaImagen4.grid(row=1, column=2)


#cambia la imagen dos
def cambiarImagen5():
    etiquetaImagen4.configure(image= imagenCambioTk6)
botonCambio2 = tk.Button(ventana, text="Cambiart", command = cambiarImagen5)
botonCambio2.grid(row=2, column=3, )



ventana.mainloop()