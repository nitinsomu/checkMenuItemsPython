import requests
import json

# endpoint
url = "https://mocki.io/v1/f6829903-01fa-4fef-8b91-c30657684fd3"

# # Username and password 
# username = "<username>"
# password = "<password>"

# payload = {
#     "username": username,
#     "password": password
# }

response = requests.get(url)

def test(responseMenu, menuItems):
    if(len(responseMenu) != len(menuItems)):
        return False
    if len(menuItems) == 0:
        return True
    
    ans = True
    for index, (childKey, childItem) in enumerate(menuItems.items()):
        ans = ans and childKey == responseMenu[index]["menuName"] and test(responseMenu[index]["children"], childItem)
    return ans


if response.status_code == 200:
    json_response = response.json()
    menuValidation = {
            "l1a" : {
                "l2a" : {}, 
                "l2b" : {}
            },
            "l1b" : {
                "l2c" : {
                    "l3a" : {},
                    "l3b" : {}
                },
                "l2d" : {},
            }
        }
    responseMenu = json_response["data"]["menuTree"]["children"]

    # print(responseMenu)
    # print(menuValidation)

    if(test(responseMenu, menuValidation)):
        print("Menu items are correct")
    else:
        print("Incorrect menu items")

else:
    print("Failed to get response. Status code:", response.status_code)

    
