from tkinter import *


def saludo():
    nombre = nombreCT.get()
    varSaludo.set("Hola " + nombre)
    



#Para indicar que "Ventana" va a ser una interfaz
ventana = Tk()

ventana.title("Primer GUI")
#tamaño de la ventana
ventana.geometry("1200x1600")
ventana.resizable(1,1)
#Color de fondo con el nombre del color en HEXADECIMAL
ventana.config(bg="#F5DA81")


marcoEntradas = LabelFrame(ventana, text="Entrada")
marcoEntradas.config(width=200, height= 200, bd= 2, relief = "raised")
marcoEntradas.pack(pady=10)
# Etiqueta para marcoEntradas
nombreE = Label(marcoEntradas, text="Nombre: ")
nombreE.grid(row= 0, column= 0, padx= 8, pady= 8)

#Caja de texto para marcoEntradas
nombreCT = Entry(marcoEntradas, width=18)
nombreCT.grid(row= 0, column= 1, padx= 8, pady= 8)

#botón para marcoEntradas
botonSaludo = Button(marcoEntradas, text="saludis", command= saludo)
botonSaludo.grid(row=1, column=0, columnspan= 2, padx=5, pady=5)

marcoSalidas = LabelFrame(ventana, text="salida")
marcoSalidas.config(width=200, height= 200, bd= 2, relief = "raised")
marcoSalidas.pack(pady=10)

# Etiqueta para marcoSalidas
varSaludo = StringVar()
saludoCT = Entry(marcoSalidas,textvariable=varSaludo, width=50, state="disabled")
saludoCT.pack(padx=10, pady=10)

# Ejecutador de la ventana principal    
ventana.mainloop()
