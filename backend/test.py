from os import environ
from pymongo import MongoClient
import requests
import urllib.request

class MongoRepo():
    def __init__(self):
        mongo_url = environ.get('MONGO_URL')
        self.db = MongoClient(mongo_url).pickmon
    def count(self):
        return self.db.pokemon.count_documents({})
    def create(self, pokemon):
        return self.db.pokemon.insert_one(pokemon)
    def delete(self, selector):
        return self.db.pokemon.delete_one(selector).deleted_count

def populate_db():
    a = MongoRepo()

    r = requests.get('https://raw.githubusercontent.com/fanzeyi/pokemon.json/master/pokedex.json')

    for item in r.json():
        a.create({'pokedex_id': item['id'], 'name': item['name']['english'], 'type': item['type']})

    print(a.count())

def save_images():
    r = requests.get('https://raw.githubusercontent.com/fanzeyi/pokemon.json/master/pokedex.json')

    for item in r.json():
        name = item['name']['english'].lower()
        poke_id = item['id']

        if poke_id < 10:
            poke_id = '00' + str(poke_id)
        elif poke_id >= 10 and poke_id < 100:
            poke_id = '0' + str(poke_id)

        print(name, poke_id)
        urllib.request.urlretrieve(f"https://assets.pokemon.com/assets/cms2/img/pokedex/full/{poke_id}.png", f"../client/public/images/pokemon/{name}.png")