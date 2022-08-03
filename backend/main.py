# -*- coding: utf-8 -*-
import json
from os import environ
from dotenv import load_dotenv
from flask import Flask, Response, request
from flask_cors import CORS
from modules.db import DB

app = Flask(__name__, static_url_path='/static')
CORS(app)
load_dotenv()

@app.route('/', methods=['GET'])
def home():
    return {'test': ['test1', 'test2', 'test3']}

@app.route('/api/pokemon', methods=['GET'])
def pokemon():
    name = request.args.get('name').capitalize()
    db = DB()
    pokemon = db.find({'name': name})
    
    print(pokemon)
    if pokemon:
        return {'pokedexId': pokemon['pokedex_id'], 'name': pokemon['name'], 'type': pokemon['type'], 'image_path': f'/api/static/images/pokemon/{pokemon["name"]}.png'}
    else:
        return Response(response=json.dumps({'error': 'Pokémon not found'}), status=404, mimetype='application/json')

@app.route('/api/random', methods=['GET'])
def random_pokemon():
    db = DB()
    pipeline = [ {'$sample': { 'size': 1 }}]

    pokemon = list(db.aggregate(pipeline))[0]
    return {'pokedexId': pokemon['pokedex_id'], 'name': pokemon['name'], 'type': pokemon['type'], 'image_path': f'/api/static/images/pokemon/{pokemon["name"]}.png'}

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5051, ssl_context=(environ.get('SERVER_CERT'), environ.get('SERVER_KEY')))
