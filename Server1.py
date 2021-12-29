import socket
from threading import Timer,Thread,Event
import json
import requests
import codecs
import datetime
import re

#Convert to utf-8 code
def UTF_ENCODE(s):
    s = re.sub(r'[àáạảãâầấậẩẫăằắặẳẵ]', 'a', s)
    s = re.sub(r'[ÀÁẠẢÃĂẰẮẶẲẴÂẦẤẬẨẪ]', 'A', s)
    s = re.sub(r'[èéẹẻẽêềếệểễ]', 'e', s)
    s = re.sub(r'[ÈÉẸẺẼÊỀẾỆỂỄ]', 'E', s)
    s = re.sub(r'[òóọỏõôồốộổỗơờớợởỡ]', 'o', s)
    s = re.sub(r'[ÒÓỌỎÕÔỒỐỘỔỖƠỜỚỢỞỠ]', 'O', s)
    s = re.sub(r'[ìíịỉĩ]', 'i', s)
    s = re.sub(r'[ÌÍỊỈĨ]', 'I', s)
    s = re.sub(r'[ùúụủũưừứựửữ]', 'u', s)
    s = re.sub(r'[ƯỪỨỰỬỮÙÚỤỦŨ]', 'U', s)
    s = re.sub(r'[ỳýỵỷỹ]', 'y', s)
    s = re.sub(r'[ỲÝỴỶỸ]', 'Y', s)
    s = re.sub(r'[Đ]', 'D', s)
    s = re.sub(r'[đ]', 'd', s)
    return s

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

RATES = []
GOLDS = []
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
   GOLDS = data['golds']

CallApi()


