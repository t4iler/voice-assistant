import requests
# I have created an account on the 'openweathermap.org' website
key2 = "f1e05a8470695ebb5754f4ec039df882"           #its my API key

api_address = 'http://api.openweathermap.org/data/2.5/weather?q=Bishkek&appid=' + key2    #website, where it takes news
json_data = requests.get(api_address).json()

def temp():
    temperature = round(json_data["main"]["temp"]-273,1)
    return temperature

def des():
    description = json_data["weather"][0]["description"]
    return description

