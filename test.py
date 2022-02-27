import requests

BASE = "http://127.0.0.1:5000/"

data = [{"name": "matchmaking", "likes":12, "views": 23},
        {"name": "restful", "likes":123, "views": 253},
        {"name": "approach", "likes":52, "views": 2663}]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i]) 
    print(response.json())


input("press enter to continue: ") # just so it pauses and we can press enter
response = requests.get(BASE + "video/20") 
print(response.json())

input("press enter to continue: ") # just so it pauses and we can press enter
response = requests.patch(BASE + "video/2", {'name':'haso'}) 
print(response.json())
