import sqlite3
from pathlib import Path

ROOT = Path(__file__).parent
NAME_SQL = 'db.sqlite3'
DATA_FOLDER = ROOT / 'data'
DB_FILE = DATA_FOLDER / NAME_SQL
CUSTOMERS = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.close()
connection.close()
