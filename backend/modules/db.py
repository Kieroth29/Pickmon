from os import environ
from pymongo import MongoClient

COLLECTION_NAME = 'pickmon'

class DB(object):
    def __init__(self):
        mongo_url = environ.get('MONGO_URL')
        self.db = MongoClient(mongo_url).pickmon

    def find_all(self, selector):
        return self.db.pokemon.find(selector)

    def find(self, selector):
        return self.db.pokemon.find_one(selector)

    def create(self, kudo):
        return self.db.pokemon.insert_one(kudo)

    def update(self, selector, kudo):
        return self.db.pokemon.replace_one(selector, kudo).modified_count

    def delete(self, selector):
        return self.db.pokemon.delete_one(selector).deleted_count
    
    def count(self):
        return self.db.pokemon.count_documents()
    
    def aggregate(self, selector):
        return self.db.pokemon.aggregate(selector)
