import sqlite3


try:
        connection = sqlite3.connect("src/database/parkDB.db")
        print(connection.total_changes,"DB-Online")

except Exception as ex:
        print(ex)
