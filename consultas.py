import sqlite3
import conexionsql3
from itertools import chain


def find_user(nombre,password):
    
    #fetchall retrieve the data 
    result = conexionsql3.connection.execute("SELECT ID, level_config FROM usuarios WHERE nombre = ? AND password = ?", (nombre,password)).fetchall()

    #Looking for data if the query its empty == no user
    try:
        first_row = next(iter(result))#iter makes list as iterator 

        return first_row
      
    except StopIteration as e:
            #Make the list 0 == No user found
            first_row = (0,0)
            return first_row 
            

