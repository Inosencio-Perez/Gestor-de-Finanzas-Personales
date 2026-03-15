import mysql.connector

def obtener_conexion():
    #Establece y retorna una conexión con la base de datos MySQL.
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Nonita100",
        database="gestor_finanzas"
    )