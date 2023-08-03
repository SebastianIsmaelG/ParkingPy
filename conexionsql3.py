import sqlite3


try:
        connection = sqlite3.connect("src/database/parkDB.db")
        print(connection.total_changes)

except Exception as ex:
        print(ex)
