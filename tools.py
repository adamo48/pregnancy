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

