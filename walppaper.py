import os
import json 
import ctypes
import requests
import random

BING_API_URL = "https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=8&mkt=en-US"
BING_BASE_URL = "https://www.bing.com"

def get_bing_wallpaper():
    response = requests.get(BING_API_URL)
    data = response.json()
    images_list = data['images']

    random_image = random.choice(images_list)

    wallpaper_url = BING_BASE_URL + random_image['url']
    return wallpaper_url

image_url = get_bing_wallpaper()

image_bytes = requests.get(image_url).content

with open("bing_wallpaper.jpg", "wb") as file:
    file.write(image_bytes)

absolute_path = os.path.abspath("bing_wallpaper.jpg")
ctypes.windll.user32.SystemParametersInfoW(20, 0, absolute_path, 3)
print("Bing daily wallpaper has been set as your desktop background.")
