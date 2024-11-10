import requests
from bs4 import BeautifulSoup
from tools import *
import re
#from string import ascii_letters

def main():
   #print(cost_ginecologist())
    print(cost_supplements())
def cost_ginecologist():
    # pakiet medyczny sredni koszt
    luxmed="https://www.luxmed.pl/dla-pacjenta/abonamenty/abonamenty-dla-doroslych-i-dzieci/pakiet-kompleksowy-zloty"
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko)' 'Chrome/41.0.2227.1 Safari/537.36'}
    responsee = requests.get(luxmed, headers=headers)
    soupo = BeautifulSoup(responsee.text, "html.parser")
    cena = soupo.find("div", class_="details__price")
    cena = cena.text
    cena = cena.replace("zÅ\x82", "").replace("Cena od ", "")
    cena = float(cena)
   # if cena:
    #print("Cena pakietu luxmed:", cena)
    #else:
            #print("Nie znaleziono ceny.")
    # ciaza na luxmed, mniejszy pakiet
    medicover = "https://www.medistore.com.pl/p/pakiet-szpitalny-prowadzenia-ciazy-3-trymestry?utm_source=porody&utm_medium=page&utm_campaign=sale&utm_content=buy%20now"
    response = requests.get(medicover)
    soup = BeautifulSoup(response.text, 'html.parser')
    price_medicover = soup.find("span", class_="price-field__value")
    price_medicover = price_medicover.text
    price_medicover = price_medicover.replace('\n',''). replace(' ','').replace('od','').replace('zł','').replace(',','.')
    price_medicover = float(price_medicover)
    return price_medicover, cena
    #ciaza na medicover, wiecej pieniedzy, ale bardziej rozbudowany
    #na NFZ za darmo przy prawidlowym przebiegu
def cost_prenatal_tests():
    nipt = "https://diag.pl/sklep/pakiety/sanco-test-prenatalny/"
    response = requests.get(nipt)
    soup = BeautifulSoup(response.text, 'html.parser')
    price = soup.find("div", class_="MuiTypography-root MuiTypography-h3 css-53tl63")
    # dodatkowy NIPT bo nikt tego nie refunduje
    # badania nie w pakiecie, platne 
    price = price.string
    price = price.replace(',','.').replace(' ','').replace('PLN','')
    price = float(price)
    return price

def cost_supplements():
    iron_ = Supplements(iron)
    iron_.fetch_price()
    iron_.price = iron_.price*3
    folic = Supplements(folic_acid)
    folic.fetch_price()
    folic.price = folic.price*3
    wit = Supplements(witD)
    wit.fetch_price()
    wit.price = wit.price*6
    dHa = Supplements(dha)
    dHa.fetch_price()
    dHa.price = dHa.price*6
    jod_1 = Supplements(jod1)
    jod_1.fetch_price()
    jod_1.price = jod_1.price*3
    jod_2 = Supplements(jod2)
    jod_2.fetch_price()
    jod_2.price = jod_2.price*6
    return iron_.price + folic.price + wit.price + dHa.price + jod_1.price + jod_2.price
    # zalecane suplementy
def cost_labour():
    private_natural_labour_cost = 9015
    private_emperors_cut_cost = 6245
    nfz_cost = 0
    labour_financing_type = get_labour_financing_type()
    if labour_financing_type == 'nfz':

        labour_type = get_labour_type()
        nfz_options = {
        1: {'description': 'Dodatkowa opieka położnej', 'price': 1500},
        2: {'description': 'Dopłata do sali rodzinnej lub jednoosobowej o podwyższonym standardzie', 'price': 500},
        3: {'description': 'Obecność osoby bliskiej przy cięciu cesarskim', 'price': 200},
        4: {'description': 'Dodatkowa opieka lekarza przy porodzie', 'price': 2000}
    }
        display_nfz_options(nfz_options)
        selected_nfz_options = get_user_selection(nfz_options)

        nfz_addons_cost = calculate_nfz_addons_cost(selected_nfz_options, nfz_options)
        nfz_cost += nfz_addons_cost
        return nfz_cost
    
    labour_type = get_labour_type()
    if labour_type == 'natura':
        return private_natural_labour_cost
    elif labour_type == 'cc':
        return private_emperors_cut_cost
    
    # cost of different painreliefs
    # cost of private labour
    
    # cost of nfz labour
    


if __name__ == "__main__":
    main()
