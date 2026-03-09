import base64
import requests
import ascii_magic
from io import BytesIO
import os

api_key = "your_key"


# get authString using base64
userpass = api_key
authString = base64.b64encode(userpass.encode()).decode()


# input the date to use
date = input("enter date (YYYY-MM-DD): ")


# specify needed data
headers = {
    "Authorization":f"Basic {authString}"
}

url = "https://api.astronomyapi.com/api/v2/studio/moon-phase"
data = {
    "format":"png",
    "style": {
        "moonStyle":"sketch"
    },

    "observer": {
        "latitude":your_latitude,
        "longitude":your_longitude,
        "date":date
    },

    "view":{
        "type":"portrait-simple",
        "orientation":"north-up"
    }
}

response = requests.post(url, json=data, headers=headers)

# get the image url
data = response.json()
moon_image_url = data['data']['imageUrl']
print(moon_image_url)


img_path = "moon_temp.png"


with open(img_path, "wb") as f:
    f.write(requests.get(moon_image_url).content)

ascii_art = ascii_magic.from_image(img_path)

ascii_str = ascii_art.to_ascii()


lines = ascii_str.split("\n")


while lines and lines[0].strip() == "":
    lines.pop(0)
while lines and lines[-1].strip() == "":
    lines.pop()

lines = [line.rstrip() for line in lines]


clean_ascii = "\n".join(lines)


print(clean_ascii)


os.remove(img_path)
