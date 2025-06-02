import requests 

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '79955b79fa7ed5873b882789a985b236'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

body_create = {
    "name": "generate",
    "photo_id": -1
}

body_change_pokemon = {
    "pokemon_id": "329921",
    "name": "New Name",
    "photo_id": -1
}

body_pokemon_in_pokebol = {
    "pokemon_id": "329921"
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

message = response_create.json()['message']
print(message)


response_change_pokemon = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change_pokemon)
print(response_change_pokemon.text)
message = response_change_pokemon.json()['message']
print(message)


response_pokemon_in_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokemon_in_pokebol)
print(response_pokemon_in_pokeball.text)
message = response_pokemon_in_pokeball.json()['message']
print(message)
