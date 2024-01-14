#Task1
import requests
import json

def download_robots(url, save_path):
    responce = requests.get(url)
    with open(save_path, "wb") as mypath:
        mypath.write(responce.content)


wikipedia_url = "https://en.wikipedia.org/robots.txt"
wikipedia_save_path = "wikipedia_robots.txt"
download_robots(wikipedia_url, wikipedia_save_path)

twitter_url = "https://twitter.com/robots.txt"
twitter_save_path = "twitter_robots.txt"
download_robots(twitter_url, twitter_save_path)

#Task2

responce1 = requests.get("https://russianwarship.rip/api/v2/war-info")

with open('warships1.json', "w") as file:
    json.dump(responce1.json(),file, indent=4)

responce2 = requests.get("https://russianwarship.rip/api/v2/statistics/latest")

with open('warships2.json', "w") as file:
    json.dump(responce2.json(),file, indent=4)

responce3 = requests.get("https://russianwarship.rip/api/v2/terms/en/artillery_systems")

with open('warships3.json', "w") as file:
    json.dump(responce3.json(),file, indent=4)
