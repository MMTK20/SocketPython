import socket 
import threading

#192.168.1.119
HOST = "127.0.0.1" #loopback
SERVER_PORT = 65432 
FORMAT = "utf8"

#Handle Client
def Client(conn: socket,addr):
    dict = conn.recv(1024).decode(FORMAT)
    conn.sendall(dict.encode(FORMAT))
    username = conn.recv(1024).decode(FORMAT)
    conn.sendall(username.encode(FORMAT))
    password = conn.recv(1024).decode(FORMAT)
    
    print("Brand: ",dict)
    print("Username:",username)
    print("Password:",password)




s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

s.bind((HOST, SERVER_PORT))
s.listen()

print("SERVER SIDE")
print("server:", HOST, SERVER_PORT)
print("Waiting for Client")

while(True):
    try:
        conn, addr = s.accept()


        thr = threading.Thread(target=Client,args=(conn,addr))
        thr.daemon = False
        thr.start()
    except:
        print("Error")
        

s.close()
