import psutil 

PROCNAME = "app.exe" 

for proc in psutil.process_iter(): # check whether the process name matches 
    if proc.name() == PROCNAME:
        print(proc)
        proc.kill() 
