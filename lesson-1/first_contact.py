import sqlite3
from pathlib import Path

ROOT = Path(__file__).parent
NAME_SQL = 'db.sqlite3'
DATA_FOLDER = ROOT / 'data'
DB_FILE = DATA_FOLDER / NAME_SQL
CUSTOMERS = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {CUSTOMERS}'  # (just translate)
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'  # INT
    'name TEXT,'  # STR
    'weight REAL'  # FLOAT
    ')'
)
connection.commit()

cursor.close()
connection.close()
