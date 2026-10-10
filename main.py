import requests

city = input("Enter city: ").strip()
url = "https://wttr.in/" + requests.utils.quote(city) + "?format=j1"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()
    current = data["current_condition"][0]
    print("City:", city)
    print("Temperature:", current["temp_C"], "°C")
    print("Feels like:", current["FeelsLikeC"], "°C")
    print("Condition:", current["weatherDesc"][0]["value"])
except requests.RequestException as exc:
    print("Request failed:", exc)
