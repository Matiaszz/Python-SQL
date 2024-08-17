import sqlite3
from main import DB_FILE, CUSTOMERS

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# Consultar dados
# * = ALL
# LIMIT 2 - traz apenas 2 resultados de toda a DB

cursor.execute(
    f'SELECT * FROM {CUSTOMERS} '
)


for row in cursor.fetchall():
    _id, name, weight = row
    print(_id, name, weight)

print()
# ------------------------------------------

# seleciona um

cursor.execute(
    f'SELECT * FROM {CUSTOMERS} '
    'WHERE id= "3" '
)
row = cursor.fetchone()
_id, name, weight = row
print(row)


cursor.close()
connection.close()
