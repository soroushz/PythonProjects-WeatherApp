import requests

location = input("Please enter a City Name: ")

def getData():   
    api_key = "9d899570aef64bc78d67f7c5e149af04"

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": location, "appid": api_key, "units": "metric"}

    response = requests.get(url, params=params)

    if response.status_code == 200: 
        data = response.json()
        return data
    else: 
        print(f"Error: {response.status_code}")
        return None

def display_weather(): 
    data = getData()
    description = data['weather'][0]['description']
    tempature = data['main']['temp']
    feelsLike = data['main']['feels_like']
    speed = data['wind']['speed']
    humidity = data['main']['humidity']

    print("Description: ", description)
    print("Temptature: ", tempature)
    print("Feels Like: ", feelsLike)
    print("Speed: ", speed)
    print("Humidity: ", humidity)

display_weather()
   

