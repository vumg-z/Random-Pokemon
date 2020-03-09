from flask import Flask, jsonify
import requests,random

app = Flask(__name__)

@app.route("/pokemon")

def pokemon():

    URL = "https://pokeapi.co/api/v2/pokemon?offset=0&limit=964"

    try:
        r = requests.get(url = URL)
        data = r.json() 

        pokemonArray = []

        for i in data['results']:
            pokemonArray.append(i['name'])

        allPokemons = len(pokemonArray)

        randomPokemon = pokemonArray[random.randint(0,allPokemons)]

        g = {}
        g["data"] = {}
        g["data"]["pokemon"] = randomPokemon

        return jsonify(g)
    
    except requests.exceptions.RequestException as e:
        return 404

