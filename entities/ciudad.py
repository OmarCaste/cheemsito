from persistence.db import get_db_connection
from mysql.connector import Error


class Ciudad:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo

    @classmethod
    def get_all(cls):
        try:
            connection = get_db_connection()
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM ciudad")
            return cursor.fetchall()
        except Error as e:
            return str(e)
        finally:
            cursor.close()
            connection.close()

    @classmethod
    def save(cls, ciudad):
        try:
            connection = get_db_connection()
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO ciudad (nombre, codigo) VALUES (%s, %s)",
                (ciudad.nombre, ciudad.codigo),
            )
            connection.commit()
            return cursor.lastrowid
        except Error as e:
            return str(e)
        finally:
            cursor.close()
            connection.close()

    @classmethod
    def update(cls, id, ciudad):
        try:
            connection = get_db_connection()
            cursor = connection.cursor()
            cursor.execute(
                "UPDATE ciudad SET nombre = %s, codigo = %s WHERE id = %s",
                (ciudad.nombre, ciudad.codigo, id),
            )
            connection.commit()
            return cursor.rowcount
        except Error as e:
            return str(e)
        finally:
            cursor.close()
            connection.close()

    @classmethod
    def delete(cls, id):
        try:
            connection = get_db_connection()
            cursor = connection.cursor()
            cursor.execute("DELETE FROM ciudad WHERE id =%s", (id))
            connection.commit()
            return cursor.rowcount
        except Error as e:
            return str(e)
        finally:
            cursor.close()
            connection.close()

    @classmethod
    def get_envios(cls):
        try:
            connection = get_db_connection()
            cursor = connection.cursor(dictionary=True)
            cursor.execute(
                "SELECT e.guia, e.fecha_hora, co.nombre AS ciudad_origen, cd.nombre AS ciudad_destino, e.estado FROM envios e JOIN ciudad co ON e.ciudad_origen_id = co.idciudad JOIN ciudad cd ON e.ciudad_destino_id = cd.idciudad"
            )
            return cursor.fetchall()
        except Error as e:
            return str(e)
        finally:
            cursor.close()
            connection.close()
