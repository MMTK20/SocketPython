
import socket

HOST = "127.0.0.1" 
PORT = 8000        
FORMAT = "utf-8"
address = (HOST,PORT)

print("CLIENT SIDE 2 ")
def sendMessage(client):
    msg = None
    while(msg!="exit"): 
        msg = input("say something : ")
        client.sendall(msg.encode(FORMAT))
        res = client.recv(1024).decode(FORMAT)
        print(res)


def startConnect():
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        hostServer = input("Sign in Host server : ")
        print("Try to connect ", hostServer, " on Port ", PORT)
        if(hostServer != HOST):
            print("WrongIP")
            return
        else:
            addressHost=(hostServer,PORT)
            client.connect(addressHost)
            print("Success connected")
            sendMessage(client)
            client.close()

startConnect()