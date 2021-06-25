import requests


def is_primo(n):
    for i in range(2, n//2):
#        print(i)
        if n%i == 0:
            return False
    
    return True

def define_primo_proximo(n):
    while True:
        if is_primo(n) == True:
            return n
        n = n + 1

def get_pokemon_type(name):
    url = "https://pokeapi.co/api/v2/type/" + name

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.json()

def get_pokemon_list(pokemons, letter):
    l = []
    for pokemon in pokemons:
        name = pokemon['pokemon']['name']
        if name.startswith(letter):
            l.append(name)
    return l

