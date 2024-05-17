import requests

def get_weather(api_key, city, units):
    # URL for the OpenWeatherMap API
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units={units}"
    
    # Send a request to the API
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        
        # Extracting relevant information
        weather = data['weather'][0]['description']
        temperature = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        
        # Determine the unit symbol
        unit_symbol = "°C" if units == "metric" else "°F"
        
        # Printing the weather details
        print(f"Weather in {city}:")
        print(f"Description: {weather}")
        print(f"Temperature: {temperature}{unit_symbol}")
        print(f"Feels Like: {feels_like}{unit_symbol}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print(f"Failed to get weather data for {city}. Error code: {response.status_code}")

if __name__ == "__main__":
    # Use the provided OpenWeatherMap API key
    api_key = '3b69cc3f8906656204c7a11b6f4abe93'
    city = input("Enter the city name: ")
    
    # Ask the user for temperature unit preference
    unit_preference = input("Choose the temperature unit (C for Celsius, F for Fahrenheit): ").strip().upper()
    units = "metric" if unit_preference == "C" else "imperial"
    
    get_weather(api_key, city, units)
