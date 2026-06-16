import requests

city = input("Enter City: ")

response = requests.get(f"https://wttr.in/{city}?format=3")

print("\nWeather Details:")
print(response.text)