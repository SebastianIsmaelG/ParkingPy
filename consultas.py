import sqlite3
import conexionsql3

def find_user(nombre,password):
    #print(nombre,password)
    #connection = sqlite3.connect("src/database/parkDB.db")
    
    result = conexionsql3.connection.execute("SELECT ID, level_config FROM usuarios WHERE nombre = ? AND password = ?", (nombre,password)).fetchall()


    print(result)