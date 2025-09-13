import requests
import time

#request urls
geocode_request_url = "https://reverse.geocoder.api.here.com/6.2/reversegeocode.json"
ISS_request_url = "http://api.open-notify.org/iss-now.json"

#geocode authentication
geocode_app_key = "hiKUvVNTRuAUCEWVyXKo"
geocode_app_secret = "ptfqAp86s5ExU7vChfk-kg"

#retrieve ISS data
ISS_response = requests.get(ISS_request_url)
ISS_data = ISS_response.json()
print("ISS Status Code:",ISS_response.status_code)

#parameters for geo payload
lat = ISS_data["iss_position"]["latitude"]
lon = ISS_data["iss_position"]["longitude"]
proximity = 250
prox_param = str(lat) + "," + str(lon) + "," + str(proximity)
payload = {
            "prox": prox_param,
            "mode": "retrieveAddresses",
            "maxresults": "1",
            "gen": "9",
            "app_id": geocode_app_key,
            "app_code": geocode_app_secret
           }

#retrieve geocode data
geo_response = requests.get(geocode_request_url, params=payload)
geo_data = geo_response.json()
print("Reverse Geo Status Code:",geo_response.status_code)

if ISS_response.status_code == geo_response.status_code == 200:
    print("\nSuccessful responses from both APIs!\n")
    try:
        city = geo_data["Response"]["View"][0]["Result"][0]["Location"]["Address"]["City"]
        country = geo_data["Response"]["View"][0]["Result"][0]["Location"]["Address"]["Country"]
    except IndexError:
        city = None
        country = None
    finally:
        status = ""
        if city and country:
            status += "The ISS is currently over: " + city + ", " + country + "\n"
        status += "ISS Latitude: " + str(lat) + "\n" + "ISS Longitude: " + str(lon)    
        print(status + "\n")






























city = geo_data["Response"]["View"][0]["Result"][0]["Location"]["Address"]["City"]
country = geo_data["Response"]["View"][0]["Result"][0]["Location"]["Address"]["Country"]








