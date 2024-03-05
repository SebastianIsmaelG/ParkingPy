import tkinter
import datetime
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

def frame_login():
    global text1, text2
    #label sesion
    etiqueta0 = tkinter.Label(ventana,text="INICIO DE SESIÓN",font=font_titulo)                      
    #label username
    etiqueta1 = tkinter.Label(ventana,text="USUARIO",anchor="w") 
    #txt username
    text1 = tkinter.Entry(ventana, width=15)
    text1.focus_set()
    #label password
    etiqueta2 = tkinter.Label(ventana,text="CONTRASEÑA",anchor="w") 
    #txt password
    text2 = tkinter.Entry(ventana, show="*", width=15) #show * allow to show password type
    
    # grid mmethod 
    # rows and columns as specified --> row down, column right
    etiqueta0.grid(row=0,column=0, columnspan=2,padx=20, pady=20)
    etiqueta1.grid(row = 1, column = 0, pady = 2)
    text1.grid(row = 1, column = 1, pady = 2)
    etiqueta2.grid(row = 2, column = 0, pady = 2)
    text2.grid(row = 2, column = 1, pady = 2)
    boton.grid(row=3,column=0, columnspan=2,padx=20, pady=20)



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
        frame_ingreso(user_ID)
        #iniciar instancia de sesion para almacenar la sesion en la db y los datos que ingresa
        #guardar datos por fecha? luego se comprueba la fecha en la que esta y vuelven los datos desde la 
        #db correspondiente al usuario que estubo logeado
        
        #El programa busca la fecha actual si hay datos con el id que esta ingresando, si no hay debe crear una nueva
        #el registro se lleva puede filtrar por las fechas y los usuarios 
        
        #tabla: id-fecha
        
            
    else:
        #normal access, verifiy data scope
        frame_ingreso(user_ID)
    
    

def frame_ingreso(user_ID):
    cerrar_login()
    ingreso = tkinter.Tk()
    ingreso.geometry("1024x768") #window default size   
    ingreso.resizable(0,0)
    ingreso.title('Ingreso')
    ingreso.iconbitmap('logo.ico')
    
    
    def timetask():
        #View date time and auto update every second
        hora_actual = datetime.datetime.now() 
        hora = datetime.datetime.strftime(hora_actual,'%d/%m/%Y %H:%M:%S')
        etiqueta3 = tkinter.Label(ingreso,text=hora)
        ingreso.after(1000, timetask)
        #label time grid
        etiqueta3.grid(row=0,column=0)
        
    ingreso.after(1000, timetask)
    
    
    
    #labels
    etiqueta4 = tkinter.Label(ingreso,text=user_ID)
    
    # grid mmethod 
    # rows and columns as specified --> row down, column right
    etiqueta4.grid(row=1,column=0)
    
 

    #print(user_ID)
     
    ingreso.mainloop()

#######################################################
def cerrar_login():
    ventana.destroy()
    
#button
boton = tkinter.Button(ventana, text ="Ingresar", command=tomar_datos )




frame_login()
ventana.mainloop()