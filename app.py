import sys
from flask import Flask, render_template, request, redirect, url_for, abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm.exc import NoResultFound
import platform
import os
from gevent.pywsgi import WSGIServer
import subprocess
import time

app = Flask(__name__, template_folder='templates')

# Creating dirs and file for a database.sqlite3

def dirnamesdb():
    
    user = os.getlogin()

    if os.path.isdir('C:\\Users\\{}\\Documents\\Partner-Register'.format(user)) == False:

        newdir = subprocess.Popen('cd C:\\Users\\{}\\Documents && mkdir Partner-Register'.format(user), stdin=subprocess.PIPE, shell=True )

    if os.path.isdir('C:\\Users\\{}\\Documents\\Partner-Register'.format(user)) == False:

        newdir1 = subprocess.Popen('cd C:\\Users\\{}\\Documents\\Partner-Register && mkdir database'.format(user), stdin=subprocess.PIPE, shell=True )
        time.sleep(1) # He puesto un cronometro de 1 segundo para que no diera error, ya que no se creaba la base de datos porque la ejecución era muy rápida
        
        file = open('C:/Users/{}/Documents/Partner-Register/database/partners.sqlite3'.format(user), 'a+')

dirnamesdb()

# Create a connection

def sqlitedb():

    if platform.system() == 'Windows':

        user = os.getlogin()
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/{}/Documents/Partner-Register/database/partners.sqlite3'.format(user)
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
        db = SQLAlchemy(app)
        
        return db
    
db = sqlitedb()

# Establishing a Table Partners for the database

class Partners(db.Model):

    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(200), nullable = False)
    dni = db.Column(db.Integer(), nullable = False, unique =True)
    email = db.Column(db.String(), nullable = False)
    direction = db.Column(db.Text(200), nullable = False)

    def __init__(self, name, dni, email, direction):

        self.name = name
        self.dni = dni
        self.email = email
        self.direction = direction

    def __str__(self):
        
        return """\
Nombre: {}
DNI: {}
Email: {}
Direction: {} """.format(self.name, self.dni, self.email, self.direction)

# Apply model Partners to the database for create the tables.

def createfile():

    user = os.getlogin()

    if platform.system() == 'Windows' and os.path.isfile('C:\\Users\\{}\\Documents\\Partner-Register\\database\\partners.sqlite3'.format(user)) == True:
        
        db.create_all()

    else:
        
        return 

createfile()

# Application backend

@app.route('/')

def home():

    return render_template('load.html')

@app.route('/register')

def register():

    return render_template('index.html')

@app.route('/submit', methods = ['POST'])

def submit():

    if request.method == 'POST':
        name = request.form['nombre']
        dni = request.form['dni']
        email = request.form['email']
        direction = request.form['direccion']

        if name == '' or dni == '' or email == '' or direction == '':
            return render_template('index.html', message5 = 'Todos los campos son obligatorios')
        
        if db.session.query(Partners).filter(dni == Partners.dni).count() == 0:

            data = Partners(name, dni, email, direction)
            db.session.add(data)
            db.session.commit()

            return render_template('success.html')
        
        return render_template('index.html', message1 = 'Ya existe un socio con el mismo DNI')

@app.route('/search')

def search():

    return render_template('search.html')

@app.route('/find', methods = ['POST'])

def find():

    if request.method == 'POST':
        dni = request.form['name']

        if dni == '':

            return render_template('search.html', message = 'Por favor introduce el DNI de un socio')

        try:

            userdni = db.session.query(Partners).filter(Partners.dni == dni).one().dni

        except NoResultFound:

            if len(dni) < 7 or len(dni) > 8:

                return render_template('search.html', message = 'DNI no válido debe contener entre 7 o 8 caracteres')

            else:
            
                return render_template('search.html', message = 'Sin resultados para el DNI: {}'.format(dni))

        else:

            if userdni == int(dni):
                
                return render_template('partnerfound.html', people = db.session.query(Partners).filter(Partners.dni == dni).one())

@app.route('/socios/<int:page_num>')

def listPartners(page_num):

    peoples = Partners.query.paginate(per_page=5, page=page_num, error_out=True)
    return render_template('partners.html', peoples=peoples)


@app.route('/test')

def test():

    return render_template('load.html')


if __name__ == '__main__':

    FLASK_ENV = 'Development'

    if FLASK_ENV == 'Development':
        
        app.run(host='localhost', port=5000, debug=True)
        
    else:

        print('Server deploy on http://localhost:5000/')
        server = WSGIServer(('localhost', 5000), app)
        server.serve_forever()
