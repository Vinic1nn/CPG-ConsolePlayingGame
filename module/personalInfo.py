import random

def genateName(race):
    if race == 'Humano':
        with open("data\\humanNames\\humanMascNames.txt", "r") as names:
            name = [line.strip() for line in names.readlines()]
        with open("data\\humanNames\\humanSurnames.txt", "r") as surnames:
            surname = [line.strip() for line in surnames.readlines()]

    # if race == 'Elfo': 
    # if race == 'Anão':

        name = random.choice(name)
        surname = random.choice(surname)
        return [name, surname]

def genateCity(): 

    with open ("data\\citiesNames\\citiesnames.txt", "r") as cities: 
        city = [line.strip() for line in cities.readlines()]
        city = random.choice(city)
    return city


names = genateName('Humano')    
city = genateCity()

print(f"Oi, eu sou {names[0]} {names[1]} de {city}")