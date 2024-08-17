import sqlite3
from pathlib import Path

ROOT = Path(__file__).parent
NAME_SQL = 'db.sqlite3'
DATA_FOLDER = ROOT / 'data'
DB_FILE = DATA_FOLDER / NAME_SQL
CUSTOMERS = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()


# CUIDADO: DELETE SEM WHERE
cursor.execute(
    f'DELETE FROM {CUSTOMERS}'
)
connection.commit()

cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name= "{CUSTOMERS}" '
)
# Cria a tabela
cursor.execute(
    # Primary key = chave que a gente vai usar para buscar valores na tabela


    f'CREATE TABLE IF NOT EXISTS {CUSTOMERS}'  # (Só traduzir)
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'  # INT
    'name TEXT,'  # STR
    'weight REAL'  # FLOAT
    ')'
)
connection.commit()

# Registrar valores na tabela

# executa UM comando SQL

sql = (
    f'INSERT INTO {CUSTOMERS} (name, weight) '
    'VALUES '
    '(?, ?)'  # valores que VÃO ser passados pelo usuario
)
print(sql)
# valores PASSADOS pelo usuario
connection.executemany(
    sql, [['Joana', 40.2], ['Allan', 2]]
)
connection.commit()

# connection.executemany('', '')  # executa MAIS DE UM comando SQL
cursor.close()
connection.close()
