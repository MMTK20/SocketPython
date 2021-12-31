import socket
import json


PORT = 3702        
FORMAT = "utf-8"
def sendList(client,list):
    msgServer = None
    list.append("end")
    for item in list:
        client.sendall(item.encode(FORMAT))
        try:
            msgServer = client.recv(1024).decode(FORMAT)
        except:
            pass
    return msgServer

def recvList(connection):
    list = []
    item = None
    msgServer = "Failed!"
    while(item != "end"):
        item = connection.recv(1024).decode(FORMAT)
        if(item != "end"):
            list.append(json.loads(item))
        else:
            return list
def sendMessage(client,option,list):
    client.sendall(option.encode(FORMAT))
    msg=client.recv(1024).decode(FORMAT)

    if(msg != option):
        return "Failed!"
    
    if(option=="login" and list !=[]):
        msgcheck=sendList(client,list)
        if(msgcheck=="okee"):
            print("Login successful!")
            return msgcheck
        else:
            print("Login unsuccessful.")
            return msgcheck

    elif(option=="register" and list !=[]):
        msgcheck=sendList(client,list)
        if(msgcheck=="okee"):
            print("Register successful!")
            return msgcheck
        else:
            print("Register unsuccessful.")
            return msgcheck

    elif(option=="info" and list !=[]):
        msgcheck=sendList(client,list)
        # for item in list:
        #     print("A:",item)
        #     client.sendall(item.encode(FORMAT))
        # if(msgcheck=="okee"):
        #     return msgcheck
        res = recvList(client)
        print("B:",res)
        # else:
        #     print("Cannot found!")
        #     return msgcheck




def startConnect(IPserver):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    IPclient = socket.gethostbyname(socket.gethostname())
    if(IPserver==IPclient):
        try:
            print("Client Side")
            addressHost=(IPserver, PORT)
            client.connect(addressHost)
            print("Client: ",client.getsockname())
            print("Success connected")
            return client
        except:
            print("Connect unsucessful")
            closeConnection(client)
    else:
        print("IP input is wrong!")
        return False

def closeConnection(client):
    off="X"
    client.sendall(off.encode(FORMAT))
    client.close()