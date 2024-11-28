import requests
import json
import datetime

def main():
     print(get_inflation(get_url()))

def get_url():
    year = datetime.datetime.now()
    year=year.year
    list_url=[]

    for x in range(10):
        year -=1
        url = "https://api-sdp.stat.gov.pl/api/1.0.0/variable/variable-data-section?id-zmienna=305&id-przekroj=739&id-rok=:rok:&id-okres=282&page-size=5000&page=0&lang=pl"
        url = url.replace(":rok:", str(year))
        list_url.append(url)
        
    return list_url
    
def get_inflation(list_url):
    another_list = []
    for url in list_url:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if target_row:= next((row for row in data["data"] if row["rownumber"] == 1), None):
                    t = float(target_row["wartosc"])-100
                    another_list.append(t)
            else:
                 return("Error")        
        else:
            return("Couldn't find the indicator. Try again later.")    
    return(sum(another_list)/10)
if __name__ == "__main__":
     main()    