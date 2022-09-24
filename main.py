
from bs4 import BeautifulSoup
import requests
import json
import time

# Retrive API key
key = "steamkey.txt"
with open(key, 'r') as file:
    key = file.read()

id = int(input("Enter User's SteamID "))


# Get the URL

page = "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=%s&steamid=%s&include_appinfo=true&format=json" % (key, id)
# Now we have the API we can search for CSS
soup = BeautifulSoup(requests.get(page).text, "html.parser")

data = json.loads(soup.text)['response']['games']

for i in data:
    if(i['appid']) == 240:
        print ("User Owns CSS")
        exit()
else:
    print("User Does Not own CSS")
