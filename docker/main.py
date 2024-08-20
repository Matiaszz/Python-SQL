import pymysql
import dotenv
import os

TABLE_NAME = 'customers'
dotenv.load_dotenv()


def env(string: str) -> str:
    return os.environ[string]


connection = pymysql.connect(
    host=env('MYSQL_HOST'),
    user=env('MYSQL_USER'),
    password=env('MYSQL_PASSWORD'),
    database=env('MYSQL_DATABASE'),
)

with connection:
    with connection.cursor() as cursor:

        # Cria a tabela se não existir
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ( '
            'id INT NOT NULL AUTO_INCREMENT, '
            'name VARCHAR(50) NOT NULL, '
            'age INT NOT NULL, '
            'PRIMARY KEY (id)'
            ') '
        )
        # LIMPA A TABELA
        cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')
    connection.commit()  # Não precisa de commit nesse caso
    # VARCHAR() - praticamente uma STRING, no caso acima,
    # a string se limita a 50 caracteres

    # MANIPULAR DADOS
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} (name, age) VALUES (%s, %s) '
        )
        data = ('Matheus', 17)
        # %s = valores que vão ser passados depois
        affectedLines = cursor.execute(sql, data)

        print(f'NUMERO DE LINHAS AFETADAS: {affectedLines}')
    connection.commit()

    # passando valores com dicionario | (%(chaveDoDicionario)s)
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} (name, age) VALUES (%(name)s, %(age)s) '
        )
        data = {'name': 'Allan', 'age': 19}
        # %s = valores que vão ser passados depois
        affectedLines = cursor.execute(sql, data)

        print(f'NUMERO DE LINHAS AFETADAS: {affectedLines}')
    connection.commit()

    # executemany com mysql
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} (name, age) VALUES (%(name)s, %(age)s) '
        )
        data = (
            {'name': 'Laura', 'age': 18},
            {'name': 'José', 'age': 43},
            {'name': 'Julia', 'age': 21},
        )

        affectedLines = cursor.executemany(sql, data)

        print(f'NUMERO DE LINHAS AFETADAS: {affectedLines}')
    connection.commit()

    # inserindo com iteraveis
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} (name, age) VALUES (%s, %s) '
        )
        data = (
            ('Luiz', 22),
            ('Otávio', 53),
            ('Miranda', 11),
        )

        affectedLines = cursor.executemany(sql, data)

        print(f'NUMERO DE LINHAS AFETADAS: {affectedLines}')
    connection.commit()
