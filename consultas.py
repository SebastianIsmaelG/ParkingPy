import sqlite3
import conexionsql3
from itertools import chain

def find_user(nombre,password):
    #print(nombre,password) 
    #fetchall retrieve the data 
    result = conexionsql3.connection.execute("SELECT ID, level_config FROM usuarios WHERE nombre = ? AND password = ?", (nombre,password)).fetchall()
    #print(result)

    #Looking for data if the query its empty == no user
    try:
        first_row = next(iter(result))#iter makes list as iterator
        for row in chain((first_row,), result): #print(row[0])
            pass # do something
            print(row[0])
    except StopIteration as e:
             # 0 results
            print("noUserIdFound")