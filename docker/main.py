import pymysql
import dotenv
import os

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
        print(cursor)
