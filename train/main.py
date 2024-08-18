import sqlite3
from pathlib import Path
import os

ROOT = Path(__file__).parent
DB = ROOT / 'train.sqlite3'
TABLE_NAME = 'train'

con = sqlite3.connect(DB)
cursor = con.cursor()


def createTable():
    cursor.execute(
        f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} '
        '('
        'ID INTEGER PRIMARY KEY AUTOINCREMENT, '
        'USER TEXT, '
        'PASSWORD TEXT'
        ')'
    )
    con.commit()


def signUp():

    userInput = input('Digite seu nome: ')

    cursor.execute(f'SELECT * FROM {TABLE_NAME}')
    con.commit()

    for _id, user, passwords in cursor.fetchall():
        if userInput in user:
            os.system('cls')
            print('Esse usuario já existe')
            return

    password = input('Digite sua senha: ')

    while len(password) <= 7:
        print('Sua senha é pequena, crie outra.')
        password = input('Digite sua senha: ')

    sql = (
        f'INSERT INTO {TABLE_NAME} (USER, PASSWORD) VALUES (:name, :password)'
    )

    cursor.execute(sql, {'name': userInput, 'password': password})
    con.commit()

    os.system('cls')


def signIn():
    userInput = input("Digite seu nome: ")
    passwordInput = input("Digite sua senha de login: ")

    cursor.execute(
        #        oq quer selecionar
        f'SELECT id, user, password FROM {TABLE_NAME} WHERE user = ?',
        (userInput,))

    result = cursor.fetchone()

    if result:
        _id, user, password_ = result
        if passwordInput == password_:
            os.system('cls')
            print("Bem-vindo de volta!")
        else:
            os.system('cls')
            print("Senha incorreta.")
    else:
        print("Usuário não encontrado.")


if __name__ == '__main__':
    createTable()

    while True:
        options = {
            '1': lambda: signIn(),
            '2': lambda: signUp(),
        }

        print('Opções: \n 1. Login \n 2. Criar conta \n 3. Sair')
        choice = input('Digite a opção: ')

        if choice == '3':
            cursor.close()
            con.close()
            exit()

        if choice in options:
            try:
                options[choice]()
            except sqlite3.Error as e:
                print(f'Erro no banco de dados: {e}')
        else:

            os.system('cls')

            print('-' * 25)
            print('Opção não encontrada.')
            print('-' * 25)
