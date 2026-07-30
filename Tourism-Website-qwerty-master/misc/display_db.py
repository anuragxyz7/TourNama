import sqlite3
from prettytable import from_db_cursor

connection = sqlite3.connect("C:\C++\hotel_website_test-main\hotel_website_test-main\instance\database.db")
cursor = connection.cursor()
cursor.execute("SELECT * FROM User")
mytable = from_db_cursor(cursor)

print(mytable)