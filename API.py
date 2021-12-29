import requests

#the required first parameter of the 'get' method is the 'url':
x = requests.get('https://tygia.com/json.php?ran=0&rate=0&gold=1&bank=VIETCOM&date=now')

#print the response text (the content of the requested file):
print(x.json())