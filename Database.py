import json


def CreateDatabase(list: list):
    user = {
        "username": list[0],
        "password": list[1],
    }

    check = False
    #ADD  new user
    with open('USER.json') as file:
        data = json.load(file)
    for users in data:
        if (list[0] == users["username"]): check=True
    
    if (check==True):print("Existed")
    else: data.append(user)
    
    #Write file
    with open('USER.json','w',encoding='ascii') as outfile:
      json_file = json.dumps(data,indent=4,ensure_ascii=False)
      print(json_file)
      outfile.write(json_file)


def checkLogin(list: list):

    check = False
    with open('USER.json') as file:
        data = json.load(file)
    
    #checking
    for users in data:
        if (list[0] == users["username"] and list[1] == users["password"]): 
            check=True
            break
    
    print(check)
    return check

newUser = ['tranhoangtin','abcdzyz']
userlogin = ['ngohuuphuc','abcdzy']

CreateDatabase(newUser)
print(checkLogin(userlogin))