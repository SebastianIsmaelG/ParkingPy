import sqlite3
import conexionsql3
from itertools import chain
import tkinter


def find_user(nombre,password):
    #print(nombre,password) 
    #fetchall retrieve the data 
    result = conexionsql3.connection.execute("SELECT ID, level_config FROM usuarios WHERE nombre = ? AND password = ?", (nombre,password)).fetchall()
    #print(result)

    #Looking for data if the query its empty == no user
    try:
        first_row = next(iter(result))#iter makes list as iterator 
        
        #Frame 2 -- Need to put this into a class or something
        ingreso = tkinter.Tk()
        ingreso.geometry("300x200") #window default size
        ingreso.title('Ingreso')
        ingreso.iconbitmap('logo.ico')

        #label datos
    except StopIteration as e:
             # 0 results
            print("noUserIdFound")