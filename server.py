import socket
import threading
import API

HOST = "127.0.0.1"
PORT = 3702       
addressofHOST = (HOST,PORT)
FORMAT = "utf-8"
client_online= []

def connectAllClient(connection, address):
  
    print("Client ", address, " connected !!!")
    print("Connection", connection.getsockname())
    temp = "running"
    client_online.append(str(address))

    # msgClient = None

    try:    
        while(temp == "running"):

            msgClient = connection.recv(1024).decode(FORMAT)
            connection.sendall(msgClient.encode(FORMAT))

            if(msgClient == "login"):
                recvList(connection, "login")
            elif(msgClient == "register"):
                recvList(connection, "register")
            elif(msgClient == "info"):
                recvList(connection, "info")
            elif(msgClient == "check"):
                pass
            else:
                temp = "stop"

        print("Client: ", address, " is disconnected !!!")
        print(connection.getsockname(), " closed !!!")
        removeAccount(connection, address)
        connection.close()
    except:
        connection.close()

def removeAccount(connection, address):
    for address in client_online:
        client_online.remove(str(address))
        connection.sendall("True".encode(FORMAT))

def recvList(connection, option):
    list = []
    item = None
    msgServer = "Failed!"
    while(item != "end"):
        item = connection.recv(1024).decode(FORMAT)
        if(item != "end"):
            list.append(item)
        else:
            # In để kiểm tra
            print(list)
            # Nếu option = 1 thì đi đến hàm login
            if(option == "login"):
                if(list != []):
                    msgServer = "okee"
            # nếu option = 0 thì đi đến hàm regis
            elif(option == "register"):
                if(list!=[]):
                    msgServer = "okee"
            elif(option =="info"):
                msgServer="okee"
        print(msgServer)
        print(option)
        connection.sendall(msgServer.encode(FORMAT))

   
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def Start():
    s.bind(addressofHOST)
    s.listen()
    print("SERVER SIDE")
    print("Server: ", addressofHOST)
    print("Waiting for Client ...")
    while True:
        try:
            global addr
            global connection
            connection, addr = s.accept()
            thread= threading.Thread(target=connectAllClient,args =(connection,addr))
            thread.daemon = False
            thread.start()
        except:
            print("Server closed!")
            closeServer(s)

            
def closeServer(s):
    s.close()

