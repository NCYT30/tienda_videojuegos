import pymysql

def obtener_conexion():
    return pymysql.connect(
        host = 'localhost',
        user= 'root',
        password = 'NCYT30',
        db = 'tienda_de_videojuegos'
    )