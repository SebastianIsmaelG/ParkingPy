import sqlite3
import conexionsql3

def find_user(nombre,password):
    
    sql = conexionsql3.conexion.sql()
    sql.execute("SELECT * FROM usuarios WHERE nombre = ? AND password = ?")