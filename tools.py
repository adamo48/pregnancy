import requests
from bs4 import BeautifulSoup
import re
def get_labour_financing_type():
    while True:
        labour_financing_type = input('Birth on nfz or private? priv|nfz: ').lower()
        if labour_financing_type in {'priv', 'nfz'}:
            return labour_financing_type
        print('Incorrect. Try again.')

def get_labour_type():
    while True:
        labour_type = input('Natural birth or cc? natural|cc: ').lower()
        if labour_type in {'natural','cc'}:
            return labour_type
        print('Incorrect. Try again.')

def display_nfz_options(options):
    print("Availiable additional options:")
    for key, value in options.items():
        print(f"{key}. {value['description']} - {value['price']} zł")
    print()

def get_user_selection(options):
    selected_options = []
    while True:
        try:
            choice = int(input("Choose a number and press enter. To finish press 0 and enter: "))
            if choice == 0:
                break
            elif choice in options:
                selected_options.append(choice)
                print(f"Choose: {options[choice]['description']} - {options[choice]['price']} zł")
            else:
                print("Incorrect. Try again.")
        except ValueError:
            print("Type correct number.")
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

class Child_budget:
    def __init__(self, stage):
        self.stage = stage
        self.expenses = {}

    def add_expenses(self, category, cost):
        category = str(category)
        self.expenses[category] = cost  

    def __str__(self):     
        return (f"{self.expenses.items()}, total:{self.expenses.values()}")
    
    #wyprawka noworodka: 
newborn = {
    "crib" : 720,
    "mattress" : 270,
    "changing_table" : 170,
    "stroller_set" : 3500,
    "linen" : 85,
    "cloth_diapers" : 25,
    "blanket" : 75
    }
#Niemowlę(0-12) 
toddler = {
    "nappies" : 2400,
    "bottle_feeding" : 5100,
    "cosmetics" : 680,
    "vaccination" : 3260,
    "clothes" : 1900,
    "chair" : 300,
    "toys" : 1700
}
#Małe dziecko(1-3)
older_toddler = {
    "food" : 4000,
    "bottle_feeding" : 1000,
    "nappies" : 1200,
    "vaccines" : 1400,
    "clothes" : 2200,
    "toys" : 2400, 
    "nursery" : 36000
}
#preschool(4-6)
preschool = {
    "public_preschool" : 7400,
    "private_preschool" : 36000,
    "clothes" : 7500,
    "food" : 4000 
}
#child(7-12)
child = {
    "public_school" : 16000,
    "private_school" : 135000,
    "additional_class" : 10000,
    "transportation" : 15000,
    "hobby" : 4500,
    "phone" : 3000,
    "computer" : 4500,
    "clothes" : 10000,
    "food" : 25000
}
#teen(13-18)
teen = {
    "public_school" : 27000,
    "private_school" : 145000,
    "additional_class" : 15000,
    "transportation" : 18000,
    "hobby" : 6000,
    "phone" : 3000,
    "computer" : 4500,
    "clothes" : 15000,
    "food" : 30000}