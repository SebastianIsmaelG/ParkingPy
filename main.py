import tkinter
import tkinter.font as tkFont

from consultas import *

ventana = tkinter.Tk()
ventana.geometry("300x200") #window default size
ventana.title('ParkingPy')
ventana.iconbitmap('C:/Users/gutie/OneDrive/Documentos/Github/ParkingPy/src/images/car_10481242.ico')

#styles
font_titulo = tkFont.Font(family="Lucida Grande", size=20,)



#label sesion
etiqueta0 = tkinter.Label(ventana,text="INICIO DE SESIÓN",font=font_titulo)

#label username
etiqueta1 = tkinter.Label(ventana,text="USUARIO",anchor="w") 
#txt username
text1 = tkinter.Entry(ventana, width=15)

#label password
etiqueta2 = tkinter.Label(ventana,text="CONTRASEÑA",anchor="w") 
#txt password
text2 = tkinter.Entry(ventana, show="*", width=15) #show * allow to show password type


#action button -> triggers tomar_datos function
def tomar_datos():
    variable_user = text1.get()
    variable_pass = text2.get()
    
    find_user(variable_user,variable_pass)
    #change the text inside the program --> etiqueta["text"] = variable

#button
boton = tkinter.Button(ventana, text ="Ingresar", command=tomar_datos )

####################################################################Frame2##############
ingreso = tkinter.Tk()
ingreso.geometry("300x200") #window default size
ingreso.title('Ingreso')
ingreso.iconbitmap('C:/Users/gutie/OneDrive/Documentos/Github/ParkingPy/src/images/car_10481242.ico')

#label datos




# grid mmethod 
# rows and columns as specified --> row down, column right
etiqueta0.grid(row=0,column=0, columnspan=2,padx=20, pady=20)
etiqueta1.grid(row = 1, column = 0, pady = 2)
text1.grid(row = 1, column = 1, pady = 2)
etiqueta2.grid(row = 2, column = 0, pady = 2)
text2.grid(row = 2, column = 1, pady = 2)
boton.grid(row=3,column=0, columnspan=2,padx=20, pady=20)







ventana.mainloop()