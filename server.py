import socket
import threading
from threading import Timer
from ENCODE import UTF_ENCODE #utf-8 encoding
from Database import CreateDatabase,checkLogin
from SearchGold import Search 
import API
import requests
import json

HOST = socket.gethostbyname(socket.gethostname())
PORT = 3702       
addressofHOST = (HOST,PORT)
FORMAT = "utf-8"
client_online= []

RATES = []
GOLDS = []
#Repeat function after 60 minutes
class perpetualTimer():

   def __init__(self,t,hFunction):
      self.t=t
      self.hFunction = hFunction
      self.thread = Timer(self.t,self.handle_function)

   def handle_function(self):
      self.hFunction()
      self.thread = Timer(self.t,self.handle_function)
      self.thread.start()

   def start(self):
      self.thread.start()

   def cancel(self):
      self.thread.cancel()

#Call API
def CallApi():
   #Call API   
   x = requests.get("https://tygia.com/json.php")

   #Decode response to convert to JSON
   decoded_data = x.text.encode().decode('utf-8-sig')
   y = json.loads(decoded_data)

   #Storage JSON file
   with open('data.json','w',encoding='ascii') as outfile:
      json_file = json.dumps(y,indent=4,ensure_ascii=False)
      outfile.write(UTF_ENCODE(json_file))

   #Load JSON file
   with open('data.json') as json_file:
      data = json.load(json_file)

   #DO STH here
   global RATES 
   RATES = data['rates']
   global GOLDS 
   GOLDS = data['golds'][0]['value']

def RepeatCalling():
    t = perpetualTimer(3600,CallApi)
    t.start()

def SendList(conn,list):
    for i in list:
        conn.sendall(i.encode(FORMAT))
        conn.recv(1024)

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
                #Res là dữ liệu tìm kiếm được từ yêu cầu của client dưới dạng list
                Res = Search(msgClient)
                SendList(connection,Res)
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
            print(list)
            if(option == "login"):
                if(list != []):
                    msgServer = "okee"
                check = checkLogin(list)
                #Nếu check = 1 thì data chính xác, =0 thì mật khẩu hoặc username sai

            elif(option == "register"):
                if(list!=[]):
                    msgServer = "okee"
                #Trong hàm CreaateDatabase nếu chưa có thông tin thì database sẽ câp nhật thêm, nếu đã tồn tại username thì print lỗi ra
                CreateDatabase(list)
            elif(option =="info"):
                msgServer="okee"
        print(msgServer)
        print(option)
        connection.sendall(msgServer.encode(FORMAT))

   
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def Start():
    s.bind(addressofHOST)
    s.listen()
    CallApi()
    print("SERVER SIDE")
    print("Server: ", addressofHOST)
    print("Waiting for Client ...")
    while True:
        try:
            global addr
            global connection

            threadCallAPI = threading.Thread(target=RepeatCalling,args=())
            threadCallAPI.daemon = False
            threadCallAPI.start()

            connection, addr = s.accept()
            thread= threading.Thread(target=connectAllClient,args =(connection,addr))
            thread.daemon = False
            thread.start()
        except:
            print("Server closed!")
            closeServer(s)

            
def closeServer(s):
    s.close()

