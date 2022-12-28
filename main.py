import tkinter

ventana = tkinter.Tk()
ventana.geometry("800x600")#tamaño ventana

#textlabel
etiqueta = tkinter.Label(ventana,text="hola mundo") #estilo texto etiqueta
etiqueta.pack()#ubicacion

#textbox
text1 = tkinter.Entry(ventana)
text1.pack()

#tomar texto con boton

#accion boton
def tomar_datos():
    variable = text1.get()
    print(variable)
    #cambiar un texto dentro del programa --> etiqueta["text"] = variable


#button
boton = tkinter.Button(ventana, text ="button", command=tomar_datos )
boton.pack()

ventana.mainloop()