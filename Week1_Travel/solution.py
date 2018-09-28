
visits = {}

def collect_places():
    global visits 
    visits = {}

    while True:
        city_country = input("Tell me where you went: ")
        
        if not city_country:
            break
        elif "," not in city_country:
            print("That's not a legal city, country combination")
            continue
        else:
            city, country = city_country.split(",")
            city = city.strip()
            country = country.strip()
            
            if country in visits:
                if city in visits[country]:
                    visits[country][city] += 1
            
                else:
                    visits[country][city] = 1
            else:
                visits[country] = {city: 1}

def display_places():
    global visits
    
    print("You visited:")
    for country in sorted(visits):
        print(country)
        for city in sorted(visits[country]):
            if visits[country][city] == 1:
                print("\t" + city)
            else:
                print("\t" + city + " ({})".format(visits[country][city]))

    visits = {}
        