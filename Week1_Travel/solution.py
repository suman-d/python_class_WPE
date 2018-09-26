
visits = {}

def collect_places():
    global visits 
    
    while True:
        city_country = input("Tell me where you went: ")
        
        if not city_country:
            break
        elif "," not in city_country:
            print("That's not a legal city, state combination")
            continue
        else:
            city, country = city_country.lower().split(",")
            city = city.strip()
            country = country.strip()
            
            if city in visits:
                visits[city][1] = visits[city][1] + 1
            else:
                visits[city] = [country, 1]
    