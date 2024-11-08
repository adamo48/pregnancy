import requests
from bs4 import BeautifulSoup

def main():
    print(cost_ginecologist())
...
def cost_ginecologist():
    # pakiet medyczny sredni koszt
    from string import ascii_letters
    luxmed="https://www.luxmed.pl/dla-pacjenta/abonamenty/abonamenty-dla-doroslych-i-dzieci/pakiet-kompleksowy-zloty"
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko)' 'Chrome/41.0.2227.1 Safari/537.36'}
    responsee = requests.get(luxmed, headers=headers)
    soupo = BeautifulSoup(responsee.text, "html.parser")
    cena = soupo.find("div", class_="details__price")
    cena = cena.text
    cena = cena.replace(" ", "")
    cena = cena.strip(ascii_letters)
    cena = cena.replace("zÅ", "")
   # if cena:
    print("Cena pakietu luxmed:", cena)
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
    return price_medicover
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
    pass
    # zalecane suplementy
def cost_labour():
    pass
    # cost of different painreliefs
    # cost of private labour
    # cost of nfz labour

if __name__ == "__main__":
    main()
