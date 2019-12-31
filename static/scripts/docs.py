import os

user = os.getlogin()

# PathApp

docs = "static\\docs\pathDocs.txt"
pathDocs = open(docs, 'w')
pathDocs.write('C:\\Users\\{}\\Documents\\Partner-Register\\scripts\\docs.exe'.format(user))
pathDocs.close()

# PathProcess

process = "static\\docs\pathProcess.txt"
pathProcess = open(process, 'w')
pathProcess.write('C:\\Users\\{}\\Documents\\Partner-Register\\scripts\\process.exe'.format(user))
pathProcess.close()
