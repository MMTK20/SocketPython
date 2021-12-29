import socket
import json

HOST = "127.0.0.1"
SERVER_PORT = 65432
FORMAT = "utf8"


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("CLIENT SIDE")
client.connect( (HOST, SERVER_PORT) )
print("client address:",client.getsockname())

data = {
                    "buy": "60,800.00",
                    "sell": "61,400.00",
                    "company": "DOJI",
                    "brand": "",
                    "updated": "2021-12-29 09:43:00",
                    "brand1": "",
                    "day": "20211229",
                    "id": "17091459",
                    "type": "AVPL / DOJI CT bu\u00f4n",
                    "code": "AVPL /  CT bu\u00f4n"
                }

print(data["buy"])
username = input("Username: ")
password = input("Password: ")

# if (not data["brand"] ) : 
#     st = data["brand"] + " "
client.sendall(json.dumps(data).encode(FORMAT))
client.recv(1024)
client.sendall(username.encode(FORMAT))
client.recv(1024)
client.sendall(password.encode(FORMAT))

input()
