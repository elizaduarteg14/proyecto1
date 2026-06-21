import pymysql

def conectar():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="FASdel47!",
        database="tarea3",
        port=3306
    )