import sqlite3
from pathlib import Path

# CRUD - CREATE  READ    UPDATE  DELETE
# SQL -  INSERT  SELECT  UPDATE  DELETE

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

# RECOMENDAVEL: DELETE COM WHERE
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
    '(:name, :weight)'  # valores que VÃO ser passados pelo usuario
)

# connection.executemany('', '')  # executa MAIS DE UM comando SQL

# valores PASSADOS pelo usuario
cursor.executemany(
    sql,
    [
        {'name': 'Allan', 'weight': 23},
        {'name': 'Maria', 'weight': 64},
        {'name': 'Davi', 'weight': 22},
        {'name': 'Mateus', 'weight': 13},
        {'name': 'Otávio', 'weight': 12},
    ]
)

connection.commit()


if __name__ == '__main__':
    print(sql)
    # DELETE COM WHERE
    cursor.execute(
        f'DELETE FROM {CUSTOMERS} '
        'WHERE id= "3" '
    )
    connection.commit()

    cursor.execute(
        f'UPDATE {CUSTOMERS} '
        'SET name="valor" '
        'WHERE id= 4 '
    )
    connection.commit()

    cursor.close()
    connection.close()
