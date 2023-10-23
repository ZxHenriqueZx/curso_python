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
    'DELETE FROM sqlite_sequence WHERE name="{customers}"'
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

cursor.execute(
    'INSERT INTO customers (id, name, weight) '
    'VALUES (NULL, "Pedro", 2.80),'
    '(NULL, "Luis Henrique", 1.80)'
)
connection.commit()

cursor.close()
connection.close()

