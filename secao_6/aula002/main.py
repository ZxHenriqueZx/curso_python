# PyMySQL - um cliente MySQL feito em Python Puro
# Doc: https://pymysql.readthedocs.io/en/latest/
# Pypy: https://pypi.org/project/pymysql/
# GitHub: https://github.com/PyMySQL/PyMySQL
import pymysql
import pymysql.cursors
import dotenv
import os

TABLE_NAME = 'customers'

dotenv.load_dotenv()

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
    cursorclass=pymysql.cursors.DictCursor,
)

with connection:
    with connection.cursor() as cursor:
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'nome VARCHAR(35) NOT NULL, '
            'idade INT NOT NULL, '
            'PRIMARY KEY (id)'
            ')'
        )
        cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')
    connection.commit()

    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) VALUES (%s, %s) '
        )

        #print(sql)

        cursor.execute(sql, ('Pedro', 18))    
        connection.commit()

    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) VALUES (%(nome)s, %(idade)s) '
        )

        #print(sql)

        data = {"nome": "João", "idade": 52}
        cursor.execute(sql, data)    
        connection.commit()

    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) VALUES (%(nome)s, %(idade)s) '
        )

        #print(sql)

        data2 = (
            {'nome':'Jamal', 'idade': 52},
            {'nome':'Joana', 'idade': 12},
            {'nome':'Kevin', 'idade': 18},
            {'nome':'Cleber', 'idade': 58},
            {'nome':'Mariza', 'idade': 13},
        )

        cursor.executemany(sql, data2)    
        connection.commit()

    with connection.cursor() as cursor:
        consult1 = 1
        consult2 = 4
        sql = (
            f'SELECT * FROM {TABLE_NAME} '
            f'WHERE id >= %s AND id <= %s'
        )

        cursor.execute(sql, (consult1, consult2))

        data3 = cursor.fetchall()

        #for row in data3:
        #    print(row)

    with connection.cursor() as cursor:
        sql = (
            f'DELETE FROM {TABLE_NAME} '
            'WHERE id = 3'
        )
        cursor.execute(sql)
        connection.commit()

        sql2 = (f'SELECT * FROM {TABLE_NAME}')
        cursor.execute(sql2)

        #for row in cursor.fetchall():
        #    print(row)

    with connection.cursor() as cursor:
        sql = (
            f'UPDATE {TABLE_NAME} '
            'SET nome=%s, idade=%s '
            'WHERE id = %s'
        )

        cursor.execute(sql, ('Mudei', 13, 4))
        connection.commit()

        sql2 = (f'SELECT * FROM {TABLE_NAME}')
        cursor.execute(sql2)

        for row in cursor.fetchall():
            print(row)

