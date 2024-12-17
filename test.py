import requests
from bs4 import BeautifulSoup
luxmed="https://www.luxmed.pl/dla-pacjenta/abonamenty/abonamenty-dla-doroslych-i-dzieci/pakiet-kompleksowy-zloty"
response = requests.get(luxmed)
soup = BeautifulSoup(response.content, "html.parser")
cena = soup.find(class_="details__price")
if cena:
        print("Cena:", cena.get_text())
else:
        print("Nie znaleziono ceny.")