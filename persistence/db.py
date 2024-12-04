import mysql.connector
from mysql.connector import Error


def get_db_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="20721Mar",
        database="cheems",
        port="3306",
    )
