import requests
import time
from datetime import datetime


while(1):
    response = requests.get("http://api.open-notify.org/iss-now.json")
    data = response.json()
    print(datetime.utcfromtimestamp(data["timestamp"]))
    print("ISS Latitude: " + data["iss_position"]["latitude"])
    print("ISS Longitude: " + data["iss_position"]["longitude"] + "\n")
    time.sleep(5)




















