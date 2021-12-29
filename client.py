import socket

HOST = "127.0.0.1" 
PORT = 3702        
FORMAT = "utf-8"
address = (HOST,PORT)

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
        if(msgcheck=="okee"):
            return msgcheck
        else:
            print("Cannot found!")
            return msgcheck


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


def startConnect():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        print("Client Side")
        addressHost=(HOST, PORT)
        client.connect(address)
        print("Client: ",client.getsockname())
        print("Success connected")
        return client
    except:
        print("Connect unsucessful")
        closeConnection(client)

def closeConnection(client):
    off="X"
    client.sendall(off.encode(FORMAT))
    client.close()