import requests
import json

FILE="https://tygia.com/json.php"

goldType=[]

respone= requests.get(FILE)
gold=json.loads(respone.content)
price = gold['golds']
golds = price[0]
value = golds['value']

for i in value:
        goldType.append(i['type'])

