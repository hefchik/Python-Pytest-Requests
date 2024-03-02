import requests
HOST = 'https://api.pokemonbattle.me/v2'
response1 = requests.post(url=f'{HOST}/pokemons',
                        json={
                        "name": "Питон",
                        "photo": "https://dolnikov.ru/pokemons/albums/007.png"
                        },
                        headers={'Content-Type': 'application/json', "trainer_token": "7d86cc52bc48152c8e77a3ff4d128927"})

print(response1.json())

response2 = requests.put(url=f'{HOST}/pokemons',
                        json={
                        "pokemon_id": response1.json()['id'],
                        "name": "Новый Питон",
                        "photo": "https://dolnikov.ru/pokemons/albums/008.png"
                        },
                        headers={'Content-Type': 'application/json', "trainer_token": "7d86cc52bc48152c8e77a3ff4d128927"})

print(response2.json())

response3 = requests.post(url=f'{HOST}/trainers/add_pokeball',
                        json={
                        "pokemon_id": response1.json()['id'],
                        },
                        headers={'Content-Type': 'application/json', "trainer_token": "7d86cc52bc48152c8e77a3ff4d128927"})

print(response2.json())