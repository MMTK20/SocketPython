import socket
import threading

HOST = "127.0.0.1"
PORT = 8000        
addressofHOST = (HOST,PORT)
FORMAT = "utf-8"


def connectAllClient(connectClient, address):
    
    connected = True
    while connected:
        msg = connectClient.recv(1024).decode(FORMAT)
        print("Client", address, "have said : ", msg)
        if(msg == "exit"):
            connected = False
    connectClient.close()


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(addressofHOST)

def Start():
    s.listen()
    while True:
            client, addr = s.accept()
            print("we have already listen to you", addr)
            thread= threading.Thread(target=connectAllClient,args =(client,addr))
            thread.daemon = False
            thread.start()


print("SERVER SIDE")
Start()
s.close()
