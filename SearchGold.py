import json
from ENCODE import UTF_ENCODE
def Search(msg):
    TYPE = UTF_ENCODE(msg[0])
    DATE = msg[1]

    res = []
    with open('data.json') as file:
        data = json.load(file)

    for gold in data['golds']:
        if (DATE == gold['date']):
            value = gold['value']
            for i in value:
                if (TYPE == i['type']): res.append(i)
    
    print(res)
    return res

msg = ['AVPL / DOJI CT buon', '20211228']
Search(msg)