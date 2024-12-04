import mysql.connector
from mysql.connector import Error

def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user= 'root',
        password= '15546BEJ',
        database= 'cheems',
        port= '53088'
    )