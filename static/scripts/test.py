import os
import subprocess
import time
import shutil

def carpeta():

    user = os.getlogin()
    dbPath = 'C:\\Users\\{}\\Documents\\Partner-Register\\database\\partners.sqlite3'.format(user)
    dbPath1 = dbPath.replace('\\', '\\')
    print(dbPath1)
    return dbPath1

dbPath1 = carpeta()




