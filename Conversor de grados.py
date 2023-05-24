# -*- coding: utf-8 -*-
"""
Created on Sun May  7 17:50:20 2023

@author: berna
"""

import tkinter as tk
#primera etiqueta
def fahrenheit():
    n=int(numero.get())
    global r
    r=((n*(9/5))+(32))
    vis.config(text=r)
   
    
def kelvin():
    n=int(numero.get())
    global t
    t=n+ 273.15
    vis2.config(text=t)
  #Segunda etiqueta
def Celcius():
    p=int(numero2.get())
    global h
    h=((p-32)*(5/9)) 
   
    vis3.config(text=h)
    
def kelvin2():
    e=int(numero2.get())
    global u
    u=((e)-(32)*(5/9)+(273.15))
   
    vis4.config(text=u)
    
    #Tercera etiqueta
def fahrenheit2():
    n=int(numero3.get())
    global r
    r=(n-273.15)*9/5 + 32
    vis6.config(text=r)
    
def Celcius2():
    p=int(numero3.get())
    global h
    h=p-273.15
   
    vis5.config(text=h)    
    
    
        
       
 
 
       
  
ventana =tk.Tk()
ventana.title("Conversor de grados")
ventana.geometry("800x800")

#Primer etiqueta
etiqueta=tk.Label(ventana, text="Calculadora de temperaturas")
etiqueta.grid(column=5, row=0)
numero=tk.Entry()
numero.grid(column=5, row=5)
etiqueta=tk.Label(ventana, text="Ingresa los grados en celcius")
etiqueta.grid(column=5, row=2)

botonaceptar=tk.Button(ventana, text="°F", command =fahrenheit)
botonaceptar.grid(column=2, row=11)
resultado = tk.Label(ventana,text="°F:")
resultado.grid(column=2, row=15)
vis =tk.Label(ventana, text ="")
vis.grid(column=2, row=20)



botonaceptar=tk.Button(ventana, text="°k", command=kelvin)
botonaceptar.grid(column=5, row=11)
resultado = tk.Label(ventana,text="°k:")
resultado.grid(column=5, row=15)
vis2 =tk.Label(ventana, text ="")
vis2.grid(column=5, row=20)

#Segunda etiqueta

numero2=tk.Entry()
numero2.grid(column=5, row=25)
etiqueta2=tk.Label(ventana, text="Ingresa los grados en Fahrenheit")
etiqueta2.grid(column=5, row=22)

botonaceptar=tk.Button(ventana, text="°C", command =Celcius)
botonaceptar.grid(column=2, row=50)
resultado = tk.Label(ventana,text="°C:")
resultado.grid(column=2, row=55)
vis3 =tk.Label(ventana, text ="")
vis3.grid(column=2, row=60)

botonaceptar=tk.Button(ventana, text="°k", command=kelvin2)
botonaceptar.grid(column=5, row=50)
resultado = tk.Label(ventana,text="°k:")
resultado.grid(column=5, row=55)
vis4 =tk.Label(ventana, text ="")
vis4.grid(column=5, row=60)

#Tercera etiqueta
numero3=tk.Entry()
numero3.grid(column=5, row=80)
etiqueta2=tk.Label(ventana, text="Ingresa los grados en Kelvin")
etiqueta2.grid(column=5, row=75)

botonaceptar=tk.Button(ventana, text="°C", command =Celcius2)
botonaceptar.grid(column=2, row=100)
resultado = tk.Label(ventana,text="°C:")
resultado.grid(column=2, row=105)
vis5 =tk.Label(ventana, text ="")
vis5.grid(column=2, row=110)

botonaceptar=tk.Button(ventana, text="°F", command =fahrenheit2)
botonaceptar.grid(column=5, row=100)
resultado = tk.Label(ventana,text="°F:")
resultado.grid(column=5, row=105)
vis6 =tk.Label(ventana, text ="")
vis6.grid(column=5, row=110)

ventana.mainloop()
