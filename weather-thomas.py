import requests


def get_sanford_weather():
  # Coordinates for Sanford, NC (Latitude: 35.4799, Longitude: -79.1803)
  url = "https://api.open-meteo.com/v1/forecast"

  params = {
      "latitude": 35.4799,
      "longitude": -79.1803,
      "daily": ["temperature_2m_max", "temperature_2m_min", "precipitation_sum"],
      "temperature_unit": "fahrenheit",
      "precipitation_unit": "inch",
      "timezone": "auto",
      "forecast_days": 2,
  }

  try:
    print("Fetching weather data for Sanford, NC...\n")
    response = requests.get(url, params=params)
    response.raise_for_status()  # Raises an error for bad HTTP codes

    data = response.json()

    # Extract daily forecast metrics
    daily = data.get("daily", {})
    dates = daily.get("time", [])
    max_temps = daily.get("temperature_2m_max", [])
    min_temps = daily.get("temperature_2m_min", [])
    precip_sums = daily.get("precipitation_sum", [])

    # Display the results nicely
    print("==========================================")
    print("   WEATHER FORECAST: SANFORD, NC")
    print("==========================================")

    for i in range(len(dates)):
      date = dates[i]
      max_t = max_temps[i]
      min_t = min_temps[i]
      precip = precip_sums[i]

      print(f"Date: {date}")
      print(f"  • High Temp : {max_t}°F")
      print(f"  • Low Temp  : {min_t}°F")
      print(f"  • Rainfall  : {precip} inches")
      print("-" * 42)

  except requests.exceptions.RequestException as e:
    print(f"Error fetching weather data: {e}")


if __name__ == "__main__":
  get_sanford_weather()