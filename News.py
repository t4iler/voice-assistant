import requests
# I have created an account on the 'newsapi.org' website
key = "2e7586b62f1c4aa1bf318fbf419ef342"    #its my API key

api_address="x" + key    #website, where it takes news
json_data = requests.get(api_address).json()

ar=[]

def news():
    for i in range(3):        # (3) definesб how much news do we want to hear
        ar.append("Number " + str(i+1) +", " + json_data["articles"][i]["title"] + ".")

    return ar

#assist = news()
