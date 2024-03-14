from flask import redirect, request
from bd import obtener_conexion

def guardar_usuario(nombre, edad, usuario, correo, contrasena, fk_rol, active):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO usuarios(nombre, edad, usuario, correo, contrasena, fk_rol, active) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                        (nombre, edad, usuario, correo, contrasena, fk_rol, active))
    conexion.commit()
    conexion.close()



def ingresar_usuario(usuario, contrasena):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM usuarios WHERE usuario = %s AND contrasena = %s", (usuario, contrasena))
        usuario_db = cursor.fetchone()
    conexion.commit()
    conexion.close()

    if usuario_db:
        return {
            'id': usuario_db[0],
            'nombre': usuario_db[1],
            'edad': usuario_db[2],
            'usuario': usuario_db[3],
            'correo': usuario_db[4],
            'contrasena': usuario_db[5],
            'fk_rol': usuario_db[6],
            'active': usuario_db[7]
        }
    else:
        return None



def obtener_juegos():
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM juegos")
            juegos = []
            column_names = [col[0] for col in cursor.description]
            for row in cursor.fetchall():
                juego = dict(zip(column_names, row))
                juegos.append(juego)
        return juegos
    except Exception as e:
        print(f"Error al obtener juegos: {e}")
        return []
    finally:
        conexion.close()


def guardar_juego(nombre_juego, precio_unitario, cantidad, fk_categoria, imagen):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("INSERT INTO juegos(nombre_juego, precio_unitario, cantidad, fk_categoria, imagen) VALUES (%s, %s, %s, %s, %s)",
                                (nombre_juego, precio_unitario, cantidad, fk_categoria, imagen))

        conexion.commit()
    except Exception as e:
        print(f"Error al insertar datos en la base de datos: {e}")
        conexion.rollback()  
    finally:
        conexion.close()




def actualizar_juego(id, nombre_juego, precio_unitario, cantidad, fk_categoria, imagen):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("UPDATE juegos SET nombre_juego=%s, precio_unitario=%s, cantidad=%s, fk_categoria=%s, imagen=%s WHERE id=%s",
                           (nombre_juego, precio_unitario, cantidad, fk_categoria, imagen, id))

        conexion.commit()
    except Exception as e:
        print(f"Error al editar datos en la base de datos: {e}")
        conexion.rollback() 
    finally:
        conexion.close()


def eliminar_juego_por_id(id_juego):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("DELETE FROM juegos WHERE id=%s", (id_juego,))
        conexion.commit()
    except Exception as e:
        print(f"Error al eliminar juego de la base de datos: {e}")
        conexion.rollback() 
    finally:
        conexion.close()



def obtener_categoria():
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM categoria")
            categoria = []
            column_names = [col[0] for col in cursor.description]
            for row in cursor.fetchall():
                cate = dict(zip(column_names, row))
                categoria.append(cate) 
        return categoria
    except Exception as e:
        print(f"Error al obtener categoría: {e}")
        return []
    finally:
        conexion.close()


def guardar_categoria(categoria, imagen):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("INSERT INTO categoria(categoria, imagen) VALUES (%s, %s)",
                                (categoria, imagen))
        conexion.commit()
    except Exception as e:
        print(f"Error al insertar datos en la base de datos: {e}")
        conexion.rollback()
    finally:
        conexion.close() 

def actualizar_categoria(id, categoria, imagen):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("UPDATE categoria SET categoria=%s, imagen=%s WHERE id=%s",
                           (categoria, imagen, id))
        conexion.commit()
    except Exception as e:
        print(f"Error al editar datos en la base de datos: {e}")
        conexion.rollback() 
    finally:
        conexion.close()


def eliminar_categoria_por_id(id_categoria):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("DELETE FROM categoria WHERE id=%s", (id_categoria,))
        conexion.commit()
    except Exception as e:
        print(f"Error al eliminar categoría de la base de datos: {e}")
        conexion.rollback() 
    finally:
        conexion.close()


def realizar_compra(id_juego, id_usuario, cantidad):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("INSERT INTO venta_juegos (fk_juego, fk_usuario, cantidad) VALUES (%s, %s, %s)",
                           (id_juego, id_usuario, cantidad))
        conexion.commit()
    except Exception as e:
        print(f"Error al realizar la compra: {e}")
        conexion.rollback()
    finally:
        conexion.close()

def restar_cantidad_juego(id_juego, cantidad):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("UPDATE juegos SET cantidad = cantidad - %s WHERE id = %s", (cantidad, id_juego))
        conexion.commit()
    except Exception as e:
        print(f"Error al restar la cantidad del juego: {e}")
        conexion.rollback()
    finally:
        conexion.close()
