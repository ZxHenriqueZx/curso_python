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

cursor.execute('DELETE FROM sqlite_sequence WHERE name="customers"')
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
    '(:name, :weight)'
)

#cursor.execute(sql, ['Luis', 1.80])
#cursor.executemany(sql, (('Luis', 1.80), ('Pedro', 1.98), ('Maria', 1.60)))
#cursor.execute(sql, {'name': 'Luis', 'weight': 1.80})
cursor.executemany(sql,
     ({'name':'Luis Henrique', 'weight': 12},
     {'name':'Pedro', 'weight': 10},
     {'name':'Gabriel', 'weight': 25},
))
connection.commit()


if __name__ == '__main__':
    cursor.execute('DELETE FROM customers WHERE id = "2"')
    connection.commit()

    cursor.execute(
        'UPDATE customers '
        'SET name="Mudei", weight=100.10 '
        'WHERE id="3"'
    )
    connection.commit()

    cursor.execute(
        'INSERT INTO customers (name, weight) '
        'VALUES ("Cuca Beludo", 50.94)'
    )
    connection.commit()

    cursor.execute('SELECT * FROM customers')
    connection.commit()

    for row in cursor.fetchall():
        _id, name, weight = row
        print(_id, name, weight) 

    cursor.close()
    connection.close()    

