import requests


def get_sanford_weather():
    # Pre-configured coordinates for Sanford, NC
    lat = 35.48
    lon = -79.18

    # Open-Meteo endpoint configured for Fahrenheit (°F) and MPH (mph)
    url = f"https://open-meteo.com{lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m,apparent_temperature,wind_speed_10m&temperature_unit=fahrenheit&wind_speed_unit=mph"

    print("⏳ Fetching atmospheric data for Sanford, NC...")

    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP request errors
        data = response.json()

        current = data["current"]
        units = data["current_units"]

        # Render parsed weather data to the terminal
        print(f"\n{"="*35}")
        print(" Live Weather: Sanford, NC ")
        print(f"{"="*35}")
        print(f"🌡️  Temperature:   {round(current['temperature_2m'])}{units['temperature_2m']}")
        print(f"🥶 Feels Like:    {round(current['apparent_temperature'])}{units['apparent_temperature']}")
        print(f"💧 Humidity:      {current['relative_humidity_2m']}{units['relative_humidity_2m']}")
        print(f"💨 Wind Speed:    {round(current['wind_speed_10m'])} {units['wind_speed_10m']}")
        print(f"{"="*35}\n")

    except requests.exceptions.RequestException as error:
        print(f"❌ Failed to retrieve weather data: {error}")


if __name__ == "__main__":
    get_sanford_weather()
