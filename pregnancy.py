import requests
def cost_ginecologist():
#pakiet medyczny średni koszt
    from bs4 import BeautifulSoup
    luxmed="https://www.luxmed.pl/dla-pacjenta/abonamenty/abonamenty-dla-doroslych-i-dzieci/pakiet-kompleksowy-zloty"
    response = requests.get(luxmed)
    soup = BeautifulSoup(response.content, "html.parser")
    cena = soup.find(class_="details__price")
    if cena:
            return("Cena:", cena.get_text())
    else:
            return("Nie znaleziono ceny.")
#ciąża na luxmed, mniejszy pakiet
    #medicover = "https://www.medistore.com.pl/p/pakiet-szpitalny-prowadzenia-ciazy-3-trymestry?utm_source=porody&utm_medium=page&utm_campaign=sale&utm_content=buy%20now"
#ciąża na medicover, więcej pieniędzy, ale bardziej rozbudowany
#na NFZ za darmo przy prawidłowym przebiegu
def cost_prenatal_tests():
    NIPT = "https://diag.pl/sklep/pakiety/sanco-test-prenatalny/"
    #dodatkowy NIPT bo nikt tego nie refunduje
    #badania nie w pakiecie, płatne 
def cost_supplements():
    ...
    #zalecane suplementy
def cost_labour():
    ...
    # cost of different painreliefs
    #cost of private labour
    #cost of nfz labour