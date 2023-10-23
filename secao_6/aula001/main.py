import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_FILE = ROOT_DIR / 'db.sqlite3'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(
    'DELETE FROM customers'
)
connection.commit()

cursor.execute(
    'CREATE TABLE IF NOT EXISTS customers'    
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)
connection.commit()

sql = (
    'INSERT INTO customers (name, weight) '
    'VALUES '
    '(?, ?)'
)

#cursor.execute(sql, ['Luis', 1.80])
cursor.executemany(sql, (('Luis', 1.80), ('Pedro', 1.98), ('Maria', 1.60)))
connection.commit()

cursor.close()
connection.close()

