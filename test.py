import requests
import json

# endpoint
url = "<endpoint>"

# Username and password
username = "<username>"
password = "<password>"

payload = {
    "username": username,
    "password": password
}

response = requests.get(url, json=payload)

def test(response_data, level1, level2):
    flag = 1
    data = response_data['data']
    menuTree = data['menuTree']
    l1Menu = menuTree['children']

    if(len(l1Menu) != (level1)): #Check length of L1 menu
        flag = 0
    
    for l1Index, l1Element in enumerate(l1Menu):
        l2Menu = l1Element['children']
        if((l1Element['menuName'] != level1[l1Index]) or (len(l2Menu)!=len(level2[l1Index]))): #Check length of L2 menu items
            flag = 0
            break
        for l2Index, l2Element in enumerate(l2Menu):
            if(l2Element['menuName'] != level2[l1Index][l2Index]):
                flag = 0
                break
        if(not flag):
            break

    if(flag): 
        print("All menu items are correct")
    else:
        print("Incorrect menu items")


if response.status_code == 200:
    json_response = response.json()
    level1 = ["l1a", "l1b"] #Level 1 Menu Items
    level2 = [["l2a", "l2b"], ["l2c", "l2d"]] #Level 2 Menu Items
    test(json_response, level1, level2)
else:
    print("Failed to get response. Status code:", response.status_code)



    
