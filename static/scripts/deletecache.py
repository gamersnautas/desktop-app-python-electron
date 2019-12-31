import getpass
import shutil
import os
import sys
import subprocess

def deletecache():

    username = getpass.getuser()

    username_tojs = open('static\\docs\\username.txt', 'w')

    username_tojs.write(username)

    username_tojs.close()

    route = os.path.abspath('C:\\Users\\{}\\AppData\\Roaming\\Python-Electron'.format(username))
    isdir = os.path.isdir(route)

    pathcache = open('static\\docs\\pathcache.txt', 'w')
    pathcache.write(route)
    pathcache.close()
    username = getpass.getuser()
    dirname = os.getcwd() # Obtenemos el directorio actual
    pathdirname = dirname.split('\\') # Lo convertimos a una lista y quitamos los separadores \\ para acceder al indice -1 que será siempre el nombre de la carpeta de nuestra app, esto lo hacemos por si la persona le cambia el nombre a la carpeta y pueda seguir borrandose la cache
    folder = pathdirname[-1]
    consoleDelete = subprocess.Popen( 'cd C:\\Users\\{}\\AppData\\Roaming && rd {} /S'.format(username, folder), stdin=subprocess.PIPE, shell=True ) 
    consoleDelete.communicate( b"S\n" ) #input

deletecache()