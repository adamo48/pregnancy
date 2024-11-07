import requests
from bs4 import BeautifulSoup

def main():
    print(cost_ginecologist())

def cost_ginecologist():
    # pakiet medyczny sredni koszt
    luxmed = "https://www.luxmed.pl/dla-pacjenta/abonamenty/abonamenty-dla-doroslych-i-dzieci/pakiet-kompleksowy-zloty"
    # ciaza na luxmed, mniejszy pakiet
    medicover = "https://www.medistore.com.pl/p/pakiet-szpitalny-prowadzenia-ciazy-3-trymestry?utm_source=porody&utm_medium=page&utm_campaign=sale&utm_content=buy%20now"
    response = requests.get(medicover)
    soup = BeautifulSoup(response.text, 'html.parser')
    price_medicover = soup.find("span", class_="price-field__value")
    price_medicover = price_medicover.text
    price_medicover = price_medicover.replace('\n',''). replace(' ','').replace('od','').replace('zł','').replace(',','.')
    price_medicover = float(price_medicover)
    # with open('output.html', 'w') as file:
    #     file.write(response.text)

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