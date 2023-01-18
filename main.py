import tkinter
import tkinter.font as tkFont

ventana = tkinter.Tk()
ventana.geometry("300x200") #tamaño ventana

#estilos 
font_titulo = tkFont.Font(family="Lucida Grande", size=20,)



#label sesion
etiqueta0 = tkinter.Label(ventana,text="INICIO DE SESIÓN",font=font_titulo)

#label username
etiqueta1 = tkinter.Label(ventana,text="USUARIO",anchor="w") #estilo texto etiqueta
#txt username
text1 = tkinter.Entry(ventana, width=15)


#label password
etiqueta2 = tkinter.Label(ventana,text="CONTRASEÑA",anchor="w") #estilo texto etiqueta
#txt password
text2 = tkinter.Entry(ventana, show="*", width=15) #show * permite mostrar tipo password, width es el ancho permitido

#tomar texto con boton
#accion boton
def tomar_datos():
    variable_user = text1.get()
    variable_pass = text2.get()
    
    #cambiar un texto dentro del programa --> etiqueta["text"] = variable


#button
boton = tkinter.Button(ventana, text ="Ingresar", command=tomar_datos )



# grid mmetodo 
# rows and columns as specified --> row hacia abajo, column hacia el lado
etiqueta0.grid(row=0,column=0, columnspan=2,padx=20, pady=20)
etiqueta1.grid(row = 1, column = 0, pady = 2)
text1.grid(row = 1, column = 1, pady = 2)
etiqueta2.grid(row = 2, column = 0, pady = 2)
text2.grid(row = 2, column = 1, pady = 2)
boton.grid(row=3,column=0, columnspan=2,padx=20, pady=20)







ventana.mainloop()