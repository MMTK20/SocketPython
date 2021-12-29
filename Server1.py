import socket
from threading import Timer,Thread,Event
import json
import requests
import codecs
import datetime

# class perpetualTimer():

#    def __init__(self,t,hFunction):
#       self.t=t
#       self.hFunction = hFunction
#       self.thread = Timer(self.t,self.handle_function)

#    def handle_function(self):
#       self.hFunction()
#       self.thread = Timer(self.t,self.handle_function)
#       self.thread.start()

#    def start(self):
#       self.thread.start()

#    def cancel(self):
#       self.thread.cancel()

# def printer():
#     print('aaaaaaaaaaaaaaaaaaaaaaaa')

# t = perpetualTimer(3,printer)
# t.start()  

# while True:
#     print('a')
    
#Call API   
x = requests.get("https://tygia.com/json.php")

#Decode response to convert to JSON
decoded_data = x.text.encode().decode('utf-8-sig')
y = json.loads(decoded_data)

#Storage JSON file
with open('data.json','w') as outfile:
   json.dump(y, outfile,indent=4)

#Load JSON file
with open('data.json') as json_file:
   data = json.load(json_file)

#DO STH here
pass
print(type(data))

