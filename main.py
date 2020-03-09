from flask import Flask, jsonify
import requests,random, pokemons
from pokemons import pokemonArray

app = Flask(__name__)

@app.route("/pokemon")

def pokemon():


    randomPokemon = pokemonArray[random.randint(0,len(pokemonArray))]

    g = {}
    g["data"] = {}
    g["data"]["pokemon"] = randomPokemon

    return jsonify(g)
    