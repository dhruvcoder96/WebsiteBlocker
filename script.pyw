import time
from datetime import datetime as dt

with open("distract_websites.txt",'r') as file1:
    distract= file1.readlines()
#print (distract)
path1 =r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,9) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,18) :
        with open(path1,"r+") as file2:
            content = file2.read()
            for x in distract:
                if not x in content:
                    file2.write(redirect + " "+ x)
        #print("work work work..")
    else:
        with open(path1,"r+") as file3:
            content = file3.readlines()
            file3.seek(0)
            for x in content:
                if not any(y in x for y in distract):
                    file3.write(x)
                else:
                    pass
            file3.truncate()
        #print("fun fun fun..")
    time.sleep(2)
