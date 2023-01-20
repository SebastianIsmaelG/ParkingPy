import sqlite3

def conexion():
    try:
        conexion = sqlite3.connect("src/database/parkDB.db")
        print("db lista")

    except Exception as ex:
        print(ex)
