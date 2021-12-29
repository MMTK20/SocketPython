import socket
import threading
from threading import Timer,Thread,Event
from ENCODE import UTF_ENCODE #utf-8 encoding
import requests
import json

HOST = "127.0.0.1"
PORT = 8000        
addressofHOST = (HOST,PORT)
FORMAT = "utf-8"

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

RATES = []
GOLDS = []
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

def Search(msg):
    list = []
    for i in GOLDS:
        if (i['type'] == 'SJC'):
             list.append(i)
    return list

def connectAllClient(connectClient, address):
    
    connected = True
    while connected:
        msg = connectClient.recv(1024).decode(FORMAT)
        print("Client", address, "have said : ", msg)
        list = Search(msg)
        connectClient.sendall(json.dumps(list[0]).encode(FORMAT))
        if(msg == "exit"):
            connected = False
    connectClient.close()


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(addressofHOST)

def Start():
    s.listen()
    CallApi()
    while True:
            threadCallAPI = threading.Thread(target=RepeatCalling,args=())
            threadCallAPI.daemon = False
            threadCallAPI.start()
        
            client, addr = s.accept()
            print("we have already listen to you", addr)
            thread= threading.Thread(target=connectAllClient,args =(client,addr))
            thread.daemon = False
            thread.start()


print("SERVER SIDE")
Start()
s.close()
