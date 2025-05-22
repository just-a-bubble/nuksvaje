LAST_CITIES_FILE = "last_cities.txt"
MAX_CITIES = 3

def save_last_city(city):
    cities = get_last_cities()

    # Odstrani če že obstaja (brez duplikatov)
    if city in cities:
        cities.remove(city)

    cities.insert(0, city)  # Dodaj novega na začetek

    # Shrani največ 3
    cities = cities[:MAX_CITIES]

    with open(LAST_CITIES_FILE, "w") as f:
        f.write(",".join(cities))

def get_last_cities():
    try:
        with open(LAST_CITIES_FILE, "r") as f:
            data = f.read().strip()
            return data.split(",") if data else []
    except FileNotFoundError:
        return []
