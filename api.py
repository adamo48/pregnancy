import requests
import json
import datetime

# URL do pobrania danych
year = datetime.datetime.now()
year=year.year
x=0
for x in range(11):
      year = year-1
      x+1
      url = "https://api-sdp.stat.gov.pl/api/1.0.0/variable/variable-data-section?id-zmienna=305&id-przekroj=739&id-rok=:rok:&id-okres=282&page-size=5000&page=0&lang=pl"
      url = url.replace(":rok:", str(year))
      print(url)
headers = {
    'X-ClientId': 'qSWq2WGJXOVsxXFcn8IJ8DYobLAbEMC73IBynhwf3RM='  # Twój klucz API
}
d

params = {
    'format': 'json',  # Format odpowiedzi
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()

target_row = next((row for row in data["data"] if row["rownumber"] == 1), None)
if target_row:
        print("Inflacja: ", float(target_row["wartosc"])-100)
else:
        print("Nie znaleziono wskaźnika.")    
