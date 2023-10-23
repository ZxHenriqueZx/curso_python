import sqlite3
from main import DB_FILE

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute('SELECT * FROM customers WHERE id= "32"')

#for row in cursor.fetchall():
#    _id, name, weight = row
#    print(_id, name, weight)
row = cursor.fetchone()
print(row)

cursor.close()
connection.close()
