import requests
from bs4 import BeautifulSoup
import re
def get_labour_financing_type():
    while True:
        labour_financing_type = input('Decydujesz się na poród prywatny czy NFZ? (priv/nfz): ').lower()
        if labour_financing_type in {'priv', 'nfz'}:
            return labour_financing_type
        print('Wprowadzono niepoprawne dane, spróbuj ponownie')

def get_labour_type():
    while True:
        labour_type = input('Poród naturalny czy cesarskie cięcie? (natura/cc)').lower()
        if labour_type in {'natura','cc'}:
            return labour_type
        print('Wprowadzono niepoprawne dane, spróbuj ponownie')

def display_nfz_options(options):
    print("Dostępne opcje dodatkowe:")
    for key, value in options.items():
        print(f"{key}. {value['description']} - {value['price']} zł")
    print()

def get_user_selection(options):
    selected_options = []
    while True:
        try:
            choice = int(input("Wybierz numer opcji i zatwierdź enterem (0, i enter aby zakończyć wybór): "))
            if choice == 0:
                break
            elif choice in options:
                selected_options.append(choice)
                print(f"Wybrano: {options[choice]['description']} - {options[choice]['price']} zł")
            else:
                print("Nieprawidłowy numer opcji. Spróbuj ponownie.")
        except ValueError:
            print("Wprowadź poprawny numer.")
    return selected_options

def calculate_nfz_addons_cost(selected_options, options):
    total = sum(options[option]['price'] for option in selected_options)
    return total
class Supplements:
        def __init__(self, url, price=0):
            self.url=url
            self.price=price
        def fetch_price(self):
            response = requests.get(self.url)
            soup = BeautifulSoup(response.text, 'html.parser')
            price_div = soup.find("div", class_="price")
            price_div=price_div.text.strip()
            pattern = r"[1-9]?[0-9]?[0-9],[0-9][0-9]"
            x = re.findall(pattern, price_div)
            self.price=x[0]
            self.price=self.price.replace(",",".")
            self.price=float(self.price)
            return {self.price}
iron = "https://www.doz.pl/apteka/p53243-Olimp_Chela-Ferr_Forte_kapsulki_30_szt."
folic_acid = "https://www.doz.pl/apteka/p65761-Olimp_Kwas_foliowy_400_g_tabletki_30_szt"
witD = "https://www.doz.pl/apteka/p126618-Vigantoletten_1000_1000_j.m._tabletki_90_szt._witamina_D"
dha = "https://www.doz.pl/apteka/p56540-Pregna_DHA_kapsulki_30_szt."
jod1 = "https://www.doz.pl/apteka/p136644-Femibion_1_Wczesna_ciaza_tabletki_powlekane_28_szt."
jod2 = "https://www.doz.pl/apteka/p121240-Prenatal_Duo_II_i_III_trymestr_ciazy_kapsulki_30_szt._Classic__60_szt._DHA"

