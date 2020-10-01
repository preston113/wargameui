from flask import Flask, request
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify
from wargame import *
import json


app = Flask(__name__)
api = Api(app)


#def obj_to_dict(obj):
  #  return obj.__dict__

CORS(app)

@app.route("/")
def hello():
    return jsonify({'text':'Hello World!'})

class Employees(Resource):
    def get(self):
        return {'employees': [{'id':1, 'name':'Balram'},{'id':2, 'name':'Tom'}]} 

class get_deck(Resource):
    def get(self):
        print('creating deck...' )
        deck1 = deck().getDeck()
        game1 = game()
        winner = game1.play_war(deck1)
        json_string = json.dumps(winner)
        return json_string
        
class play_round(Resource):
    def get(self):
        print(f"playing round number {round}")
        deck2 = deck().getDeck()
        game1 = game()
        a_cards = deck2[:len(deck2)//2]
        b_cards = deck2[len(deck2)//2:]
        winner = game1.play_round(a_cards, b_cards)
        json_string = json.dumps(winner)
        return json_string

api.add_resource(get_deck, '/get_deck') # Route_1
api.add_resource(play_round, '/play_round') # Route_1
#api.add_resource(Employees_Name, '/employees/<employee_id>') # Route_3


if __name__ == '__main__':
   app.run(port = 5002)

