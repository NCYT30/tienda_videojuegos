from wsgiref.simple_server import WSGIServer
from flask import Flask, render_template, redirect, request, session, jsonify, url_for
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from controlador import guardar_usuario, ingresar_usuario, guardar_juego, guardar_categoria, obtener_juegos, obtener_categoria, actualizar_juego
from controlador import eliminar_juego_por_id, actualizar_categoria, eliminar_categoria_por_id
import secrets
import hashlib
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

app.secret_key = secrets.token_hex(16)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")

@app.route("/home")
def home():
    juegos = obtener_juegos()
    return render_template('home.html', juegos = juegos)

@app.route("/admin")
def admin():
    return render_template('admin.html')

@app.route("/adminjuegos")
def adminjuegos():
    juegos = obtener_juegos()
    return render_template('adminjuegos.html', juegos = juegos)

@app.route("/admincategoria")
def admincategoria():
    categoria = obtener_categoria()
    return render_template('admincategoria.html', categoria = categoria)

@app.route("/crearjuego")
def crearjuego():
    return render_template('crearjuego.html')

@app.route("/perfil")
def perfil():
    return render_template('perfil.html')

@app.route("/categoria")
def categoria():
    categoria = obtener_categoria()
    return render_template('categoria.html', categoria = categoria)

@app.route("/juegos")
def juegos():
    juegos = obtener_juegos()
    return render_template('misjuegos.html', juegos = juegos)


@app.route("/crear")
def crear():
    return render_template('crear-cuenta.html')



@app.route('/guardarUsuario', methods=["POST"])
def guardarUsuario():
    nombre = request.form["nombre"]
    edad = request.form["edad"]
    usuario = request.form["usuario"]
    correo = request.form["correo"]
    password = request.form["contrasena"]
    contrasena = hashlib.sha512(password.encode('utf-8')).hexdigest()
    fk_rol = 2
    active = 0
    guardar_usuario(nombre, edad, usuario, correo, contrasena, fk_rol, active)
    
    return redirect('/juegos')
    
@app.route('/editar_juego', methods=["POST"])
def editar_juego():
    id_juego = request.form["id_juego"]
    nombre_juego = request.form["nombre_juego"]
    precio_unitario = request.form["precio_unitario"]
    cantidad = request.form["cantidad"]
    fk_categoria = request.form["fk_categoria"]

    if 'imagen' not in request.files:
        flash('No se ha seleccionado un archivo')
        return redirect(request.url)

    imagen = request.files['imagen']
    
    if imagen.filename == '' or not allowed_file(imagen.filename):
        flash('Archivo no válido. Debe ser una imagen (png, jpg, jpeg, gif)')
        return redirect(request.url)
    
    filename = secure_filename(imagen.filename)
    imagen.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    
    actualizar_juego(id_juego, nombre_juego, precio_unitario, cantidad, fk_categoria, filename)
    
    return redirect('/juegos')



@app.route('/guardarJuego', methods=["POST"])
def guardarJuego():
    nombre_juego = request.form["nombre_juego"]
    precio_unitario = request.form["precio_unitario"]
    cantidad = request.form["cantidad"]
    fk_categoria = request.form["fk_categoria"]
    
    if 'imagen' not in request.files:
        flash('No se ha seleccionado un archivo')
        return redirect(request.url)

    imagen = request.files['imagen']
    
    if imagen.filename == '' or not allowed_file(imagen.filename):
        flash('Archivo no válido. Debe ser una imagen (png, jpg, jpeg, gif)')
        return redirect(request.url)
    
    filename = secure_filename(imagen.filename)
    imagen.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    
    guardar_juego(nombre_juego, precio_unitario, cantidad, fk_categoria, filename)
    
    return redirect('/adminjuegos')


@app.route('/eliminar_juego', methods=['POST'])
def eliminar_juego():
    id_juego = request.json['id']
    eliminar_juego_por_id(id_juego)
    return jsonify({'message': 'Juego eliminado correctamente'}), 200


@app.route('/guardarCategoria', methods = ["POST"])
def guardarCategoria():

    categoria = request.form["categoria"]

    if 'imagen' not in request.files:
        flash('No se ha seleccionado un archivo')
        return redirect(request.url)

    imagen = request.files['imagen']
    
    if imagen.filename == '' or not allowed_file(imagen.filename):
        flash('Archivo no válido. Debe ser una imagen (png, jpg, jpeg, gif)')
        return redirect(request.url)
    
    filename = secure_filename(imagen.filename)
    imagen.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    
    guardar_categoria(categoria, filename)

    return('/admincategoria')


@app.route('/editar_categoria', methods=["POST"])
def editar_categoria():
    print("Llamando a la función editar_categoria")  # Agregar esta línea para imprimir en la consola
    id = request.form["id_cate"]  # Cambiado a "id_cate"
    categoria = request.form["categoria"]

    if 'imagen' not in request.files:
        flash('No se ha seleccionado un archivo')
        return redirect(request.url)

    imagen = request.files['imagen']
    
    if imagen.filename == '' or not allowed_file(imagen.filename):
        flash('Archivo no válido. Debe ser una imagen (png, jpg, jpeg, gif)')
        return redirect(request.url)
    
    filename = secure_filename(imagen.filename)
    imagen.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    
    actualizar_categoria(id, categoria, filename)
    
    return redirect('/categoria')


@app.route('/eliminar_categoria', methods=['POST'])
def eliminar_categoria():
    id_categoria = request.json['id']
    eliminar_categoria_por_id(id_categoria)
    return jsonify({'message': 'Categoría eliminada correctamente'}), 200


@app.route('/comprar', methods=['POST'])
def comprar():
    if 'usuario' in session:
        usuario = session['usuario']
        usuario_db = obtener_usuario(usuario)
        if usuario_db['fk_rol'] == 2:

            id_juego = request.form['id_juego']
            cantidad = request.form['cantidad']
            realizar_compra(id_juego, usuario_db['id'], cantidad)

            restar_cantidad_juego(id_juego, cantidad)
            return redirect('/juegos')
        else:

            return render_template('no_comprar.html')
    else:

        return render_template('login.html', mensaje='Debe iniciar sesión para comprar')



@app.route("/login")
def login():
    return render_template('login.html')


@app.route('/inlogin', methods=['POST'])
def inlogin():
    usuario = request.form['usuario']
    contrasena = request.form['contrasena']
    contrasena_hash = hashlib.sha512(contrasena.encode('utf-8')).hexdigest()

    usuario_db = ingresar_usuario(usuario, contrasena_hash)

    if usuario_db is not None:
        session['usuario'] = usuario
        session['logged_in'] = True  # Establecer la variable de sesión 'logged_in' como True
        if usuario_db['fk_rol'] == 1:
            return redirect('/admin')
        elif usuario_db['fk_rol'] == 2:
            return redirect('/home')
    else:
        return render_template('login.html', mensaje='Credenciales incorrectas')



@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return render_template('login.html')
    