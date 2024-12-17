import requests
from bs4 import BeautifulSoup
from tools import *
import datetime

def main():
    ginekolog =  cost_ginecologist()
    suplementy = cost_supplements()
    prenatalne_badania = cost_prenatal_tests()
    ciaza = cost_labour()
    total_labour = ginekolog + suplementy + prenatalne_badania + ciaza
    # print(f'Total cost of labour is: {total_labour} PLN')
    dziecko = cost_child_stages()
    print(f"Cost of labour & birth: {total_labour} PLN \nCost of raising a child (including pregnancy and labour): {dziecko + total_labour} PLN")
    

def cost_ginecologist():
    # pakiet medyczny sredni koszt
    luxmed="https://www.luxmed.pl/dla-pacjenta/abonamenty/abonamenty-dla-doroslych-i-dzieci/pakiet-kompleksowy-zloty"
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko)' 'Chrome/41.0.2227.1 Safari/537.36'}
    responsee = requests.get(luxmed, headers=headers)
    soupo = BeautifulSoup(responsee.text, "html.parser")
    cena = soupo.find("div", class_="details__price")
    cena = cena.text
    cena = cena.replace("zÅ\x82", "").replace("Cena od ", "")
    cena = float(cena)*9
    # ciaza na luxmed, mniejszy pakiet
    medicover = "https://www.medistore.com.pl/p/pakiet-szpitalny-prowadzenia-ciazy-3-trymestry?utm_source=porody&utm_medium=page&utm_campaign=sale&utm_content=buy%20now"
    response = requests.get(medicover)
    soup = BeautifulSoup(response.text, 'html.parser')
    price_medicover = soup.find("span", class_="price-field__value")
    price_medicover = price_medicover.text
    price_medicover = price_medicover.replace('\n',''). replace(' ','').replace('od','').replace('zł','').replace(',','.')
    price_medicover = float(price_medicover)
    while True:
        what_kind_prenatal_care = input("Do you want to calculate cost of private medical care? yes|no: ").lower()
        if what_kind_prenatal_care == "yes":
            print("What kind of package do you choose? \nLux-medium size, you might have to pay a little extra for additional tests/exams. \nMed-should cover almost all your needs, which can be helpful with difficult pregnancy.")
            while True:
                package = input("Choose lux|med: ").lower()
                if package in {'lux','med'}:
                    if package == 'lux':
                        return cena
                    elif package == 'med':
                        return price_medicover    
                print("Incorrect. Answer lux or med.")
        elif what_kind_prenatal_care == "no":
            cost_nfz = 0
            return cost_nfz
        print("Incorrect. Try again.")    
     
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
    while True:
        choice = input('do you want to include cost of NIPT test? yes|no: ').lower()
        if choice == 'yes':
            return price
        elif choice == 'no':
            return 0
        print('Incorrect. Try again.')
    

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
    return round(iron_.price + folic.price + wit.price + dHa.price + jod_1.price + jod_2.price, 2)
    # zalecane suplementy
def cost_labour():
    private_natural_labour_cost = 9015
    private_emperors_cut_cost = 6245
    nfz_cost = 0
    labour_financing_type = get_labour_financing_type()
    if labour_financing_type == 'nfz':

        labour_type = get_labour_type()
        nfz_options = {
        1: {'description': 'Additional midwife care', 'price': 1500},
        2: {'description': 'Cost of private room/family room', 'price': 500},
        3: {'description': 'Presence of family member during cesarean section', 'price': 200},
        4: {'description': 'Additional doctors care during birth', 'price': 2000}
    }
        display_nfz_options(nfz_options)
        selected_nfz_options = get_user_selection(nfz_options)

        nfz_addons_cost = calculate_nfz_addons_cost(selected_nfz_options, nfz_options)
        nfz_cost += nfz_addons_cost
        return nfz_cost
    
    labour_type = get_labour_type()
    if labour_type == 'natural':
        return private_natural_labour_cost
    elif labour_type == 'cc':
        return private_emperors_cut_cost
    
    # cost of different painreliefs
    # cost of private labour
    
    # cost of nfz labour
    
def get_url():
    year = datetime.datetime.now()
    year=year.year
    list_years_url=[]

    for x in range(10):
        year -=1
        url = "https://api-sdp.stat.gov.pl/api/1.0.0/variable/variable-data-section?id-zmienna=305&id-przekroj=739&id-rok=:rok:&id-okres=282&page-size=5000&page=0&lang=pl"
        url = url.replace(":rok:", str(year))
        list_years_url.append(url)
        
    return list_years_url
    
def get_inflation(list_years_url):
    list_url = []
    for url in list_years_url:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if target_row:= next((row for row in data["data"] if row["rownumber"] == 1), None):
                    t = float(target_row["wartosc"])-100
                    list_url.append(t)
            else:
                 return("Error")        
        else:
            inflation = 0
            return f"Couldn't reach the indicator. All calculations will be made with inflation = {inflation}. To reach the indicator try again."
             
    inflation = (sum(list_url)/10)
    inflation = float(inflation/100)
    return inflation
inflation = get_inflation(get_url())

def calc_newborn():

    infant = Child_budget("Newborn")  
    for keys, values in newborn.items():      
        infant.add_expenses({keys},{values})
    for key, value in newborn.items():  
        print(f"{key}: {value}")
    total_newborn = sum(newborn.values())
    years = 1
    total_newborn*=(1+inflation)**years
    return total_newborn

def calc_toddler():
    small_child = Child_budget("Toddler")  
    for keys, values in toddler.items():      
        small_child.add_expenses({keys},{values})
    for key, value in toddler.items():  
        print(f"{key}: {value}")
    total_toddler = sum(toddler.values())
    years = 1
    total_toddler*=(1+inflation)**years
    return total_toddler

def calc_older_toddler():
    small_child_2 = Child_budget("Toddler 4-6")  
    for keys, values in older_toddler.items():      
        small_child_2.add_expenses({keys},{values})
    for key, value in older_toddler.items():  
        print(f"{key}: {value}")
    total_older_toddler = sum(older_toddler.values())
    years = 2
    total_older_toddler*=(1+inflation)**years
    return total_older_toddler 

def calc_preschool():
    preschooler = Child_budget("Preschooler")  
    for keys, values in preschool.items():      
        preschooler.add_expenses({keys},{values})
    for key, value in preschool.items():  
        print(f"{key}: {value}")
    total_preschool = sum(preschool.values())
    years = 3
    total_preschool*=(1+inflation)**years
    return total_preschool 

def calc_child():
    a_child = Child_budget("Child")  
    for keys, values in child.items():      
        a_child.add_expenses({keys},{values})
    for key, value in child.items():  
        print(f"{key}: {value}")
    total_child = sum(child.values())
    years = 6
    total_child*=(1+inflation)**years
    return total_child

def calc_teen():
    teenager = Child_budget("Teenager")  
    for keys, values in teen.items():      
        teenager.add_expenses({keys},{values})
    for key, value in teen.items():  
        print(f"{key}: {value}")
    total_teen = sum(teen.values())
    years = 5
    total_teen*=(1+inflation)**years
    return total_teen

def cost_child_stages():    
    stage_of_child = input("Do you currently have a child? Type yes|no: ").lower()
    private = input("Do you want to calculate cost of private schools? Type yes|no: ").lower()
    if stage_of_child=="yes":
        what_stage=int(input("Input age of a child in years: "))
        if what_stage<1:
            if private =="yes":
                del preschool["public_preschool"]
                del child["public_school"]
                del teen["public_school"]
                return round(calc_newborn()+calc_toddler()+calc_older_toddler()+calc_preschool()+calc_child()+calc_teen(),2)

            else:
                del preschool["private_preschool"]
                del child["private_school"]
                del teen["private_school"]
                return round(calc_newborn()+calc_toddler()+calc_older_toddler()+calc_preschool()+calc_child()+calc_teen(),2)
        elif 0<what_stage<4:
            if private =="yes":
                del preschool["public_preschool"]
                del child["public_school"]
                del teen["public_school"]
                return round(calc_older_toddler()+calc_preschool()+calc_child()+calc_teen(),2)
            else:
                del preschool["private_preschool"]
                del child["private_school"]
                del teen["private_school"]
                return round(calc_older_toddler()+calc_preschool()+calc_child()+calc_teen(),2)
        elif 3<what_stage<7:
            if private =="yes":
                del preschool["public_preschool"]
                del child["public_school"]
                del teen["public_school"]
                return round(calc_preschool()+calc_child()+calc_teen(),2)
            else:
                del preschool["private_preschool"]
                del child["private_school"]
                del teen["private_school"]
                return round(calc_preschool()+calc_child()+calc_teen(),2)
        elif 6<what_stage<13:
            if private =="yes":
                del child["public_school"]
                del teen["public_school"]
                return round(calc_child()+calc_teen(),2)
            else:
                del child["private_school"]
                del teen["private_school"]
                return round(calc_child()+calc_teen(),2)
        elif 12<what_stage<19:
            if private =="yes":
                del teen["public_school"]
                return round(calc_teen(),2)
            else:
                del teen["private_school"]
                return round(calc_teen(),2)              
    elif stage_of_child == "no":
        if private =="yes":
                del preschool["public_preschool"]
                del child["public_school"]
                del teen["public_school"]
                return round(calc_newborn()+calc_toddler()+calc_older_toddler()+calc_preschool()+calc_child()+calc_teen(),2)

        else:
                del preschool["private_preschool"]
                del child["private_school"]
                del teen["private_school"]
                return round(calc_newborn()+calc_toddler()+calc_older_toddler()+calc_preschool()+calc_child()+calc_teen(),2)

           


if __name__ == "__main__":
    main()
