# Se importan los frameworks 
from flask import Flask, g, render_template, request, redirect, url_for, session, json, jsonify
#from flask login
from flask_mysqldb import MySQL,MySQLdb
import pymysql

# Nombre de la aplicación para la ejecución 
app = Flask(__name__)

# sesion
app.secret_key = 'mysecretkey'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'owldb_v1'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)


# Clase de usuarios
class user:
    def __init__(self,id, nom_usuario , correo, password):
        self.id = id
        self.nom_usuario = nom_usuario
        self.correo = correo
        self.password = password
    def __repr__(self):
        return '<User:{self.nom_usuario}>'

#Objeto de la clase usuarios
users=[]

# Inicio de la web (index, hub, hobby)
@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        #
        return render_template('index.html')
    return render_template('index.html')

# Uso de prueba para la conexión de la base de datos
@app.route('/singup', methods=['GET','POST'])
def singup(): 
    if request.method=='POST':
        #id_usuario = request.form['id_usuario']
        aux_nom_usuario = request.form['nom_usuario']
        aux_nombre = request.form['nombre']
        aux_ap_paterno = request.form['ap_paterno']
        aux_ap_materno = request.form['ap_materno']
        aux_correo = request.form['correo']
        aux_passw = request.form['passw']
        
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='owldb_v1' )
        cursor = conn.cursor()
        #GET usuario
        cursor.execute('select nom_usuario from usuarios where nom_usuario=%s', (aux_nom_usuario))
        comp_u=cursor.fetchone()
        #GET correo 
        cursor.execute('select correo from usuarios where correo=%s', (aux_correo))
        comp_c=cursor.fetchone()
        #Comprobar usuario 
        if comp_u is not None:
            error="Usuario no está dispoible"
            return render_template("error_usuario.html", des_error=error, paginaant='/singup')
        #Comprobar correo
        elif (comp_c is not None):
            error="Correo no está dispoible"
            return render_template("error_usuario.html", des_error=error, paginaant='/singup')
        #Comprobar ambos (puede ser un poco inutil, posible de descartar)
        elif (comp_u and comp_c is not None):
            error="Usuario y correo no están dispoibles"
            return render_template("error_usuario.html", des_error=error, paginaant='/singup')
        #Fin de validación; Hacer alta
        else:
            cursor.execute('insert into usuarios '
                        ' (nom_usuario, nombre, ap_paterno, ap_materno, correo, passw) '
                        ' VALUES (%s, %s, %s, %s, %s, %s) ', 
                        (aux_nom_usuario, aux_nombre, aux_ap_paterno, aux_ap_materno, aux_correo, aux_passw))
        conn.commit()
        conn.close()
    return render_template('singup.html')

# Obtener id de la sesión
def get_session():
    id=session.get('id_usuario')    
    if id is not None and (id, (int, float)):
        id= int(id)
        return(print(id))
    return id

# Módulo para iniciar sesión 
@app.route('/login', methods=['GET','POST'])
def login():
    session.pop('id_usuario', None)
    if request.method=='POST':
        correo = request.form['correo']
        passw = request.form['passw']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='owldb_v1' )
        cursor = conn.cursor()
        
        #Verificación de usario 
        cursor.execute('select id_usuario, nom_usuario, passw from usuarios where correo=%s and passw=%s', (correo, passw))
        usuario=cursor.fetchone()        
        if (usuario==None):
            #en caso de error
            conn.close()
            error="usuario y/o contraseña no son conrrectos"
            return render_template("error_usuario.html", des_error=error, paginaant='/login')
        elif (usuario=='admin'):
            session['admin']=usuario[0]        
            print(session)
            get_session()
            return render_template('index.html')
        else:
            #en caso de que jale 
            session['id_usuario']=usuario[0]        
            print(session)
            get_session()
            return render_template('index.html')
        
    return render_template('login.html')

# Cerrar sesión
@app.route('/logout')
def logout():
    session.clear()
    print(session)
    return render_template("login.html")

# Módulo de pacientes 
@app.route('/pacientes', methods=['GET', 'POST'])
def pacientes():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='owldb_v1')
    cursor = conn.cursor()
    cursor.execute=('select nombre_cliente, ap_pa, ap_ma, fecha_nacimiento, genero from Paciente order by Paciente')
    #datos = cursor.fetchall()
    conn.close()
    print (session)
    
    return render_template('prueba1.html')#, paciente=datos)



# Módulo para agregar pacientes
@app.route('/agr_pacientes/', methods=['GET', 'POST'])
def agr_pacientes():
    if request.method=='POST':
        nombre_paciente = request.form['nom_cliente']
        ap_pa = request.form['ap_pa']
        ap_ma = request.form['ap_ma']
        fecha_nacimiento = request.form['fecha_nacimiento']
        genero = request.form['genero']
        
       
        
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='owldb_v1')
        cursor = conn.cursor('insert into Paciente (nom_cliente,)')
        datos = cursor.fetchall();
        print(datos)
    return render_template('pureba1.html')



# fin del programa
if __name__ == '__main__':
    app.run(port=5000,debug=True)
    
    #En caso de cambiar el port, notificar al resto del equipo