import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENWEATHER_API_KEY")

while True:
    city = input("\nEnter city name or type exit: ")

    if city.lower() == "exit":
        print("Thank you for using Weather Agent.")
        break

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)

    print("API Status Code:", response.status_code)

    data = response.json()

    print("API Response:", data)

    if data["cod"] == 200:
        print("\nWeather Report")
        print("City:", data["name"])
        print("Temperature:", data["main"]["temp"], "°C")
        print("Feels Like:", data["main"]["feels_like"], "°C")
        print("Humidity:", data["main"]["humidity"], "%")
        print("Weather:", data["weather"][0]["description"])
        print("Wind Speed:", data["wind"]["speed"], "m/s")
    else:
        print("City not found. Try again.")