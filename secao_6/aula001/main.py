import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_FILE = ROOT_DIR / 'db.sqlite3'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(
    'CREATE TABLE IF NOT EXISTS customers'    
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)
connection.commit()

cursor.close()
connection.close()

