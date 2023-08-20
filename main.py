import tkinter
from tkinter.messagebox import *
import tkinter.font as tkFont

from consultas import *

ventana = tkinter.Tk()
ventana.eval('tk::PlaceWindow . center')
ventana.geometry("300x200") #window default size
ventana.title('ParkingPy')
ventana.iconbitmap('logo.ico')

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
    
    data = find_user(variable_user,variable_pass)
    #change the text inside the program --> etiqueta["text"] = variable
    #Now we have 2 rows 0 = ID and 1 = level config
    
    user_ID = data[0]
    user_lvl_config = data[1]
    
    if(user_ID == 0 and user_lvl_config == 0 ):
        #no user found, info message
        tkinter.messagebox.showinfo(title="Informacion", message="Comprobar usuario y/o contraseña")
       
    elif (user_lvl_config == 1):
        #admin
        cerrar_ventana()
        frame_ingreso(user_ID)
        
            
    else:
        #normal access, verifiy data scope
        cerrar_ventana()
        frame_ingreso(user_ID)
    
    



def frame_ingreso(user_ID):
        #Frame 2 -- Need to put this into a class or something
        ingreso = tkinter.Tk()
        ingreso.eval('tk::PlaceWindow . center')
        ingreso.geometry("300x200") #window default size
        ingreso.title('Ingreso')
        ingreso.iconbitmap('logo.ico')
        print(user_ID)
        
        
        
def cerrar_ventana():
    ventana.destroy()
    
#button
boton = tkinter.Button(ventana, text ="Ingresar", command=tomar_datos )





# grid mmethod 
# rows and columns as specified --> row down, column right
etiqueta0.grid(row=0,column=0, columnspan=2,padx=20, pady=20)
etiqueta1.grid(row = 1, column = 0, pady = 2)
text1.grid(row = 1, column = 1, pady = 2)
etiqueta2.grid(row = 2, column = 0, pady = 2)
text2.grid(row = 2, column = 1, pady = 2)
boton.grid(row=3,column=0, columnspan=2,padx=20, pady=20)







ventana.mainloop()