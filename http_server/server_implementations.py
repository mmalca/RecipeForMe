__author__ = 'mmalca'

import json
##from urlparse import urlparse
##from urlparse import urlparse, parse_qs
from urllib.parse import urlparse, parse_qs
from db import db_operations
from algorithm import algorithm

def get_ingredients_list(self):
    self.send_response(200)
    self.send_header('Access-Control-Allow-Origin', '*')
    self.send_header('Content-Type', 'application/json')
    self.end_headers()

    #on DB need to add "similar_ing": [1, 2, 3, 4]
    db_response = db_operations.get_ingredients_list() ##getting only the id and name
    print("db response:")
    list = []
    for i in db_response:
        list.append(i)


    #     {
    #         "ingredients": [
    #             {
    #                 "_id": 1,
    #                 "name": "tomato"
    #             },
    #             {
    #                 "_id": 2,
    #                 "name": "oil"
    #             }
    #         ]
    # }
    # json_string = json.dumps()
    self.wfile.write(json.dumps(list).encode('utf-8')) #on client side need to decode: json_from_server.decode('utf_8')
    print("sent json")

def get_recipe(self):
    ## need to get json: list of ids that represents the ingredients list from user
    #content_len = int(self.headers.get('Content-Length'))
    #json_ingredients_list = self.rfile.read(content_len) #Readin the data into json_ingredients_list (need to decode?)

    #### Option1:
    ##query = urlparse(self.path).query ## parsing the query of the GET request
    ##query_components = dict(qc.split("=") for qc in query.split("&"))
    ## imsi = query_components["imsi"] ## to pull a specific parameter named "imsi"

    #### Option2:
    query_components = parse_qs(urlparse(self.path).query)
    ingredients_from_user = query_components["ingredients"]
    ing_list_int = []

    ing_list_str = ingredients_from_user[0].split(",")
    for ing in ing_list_str:
        ing_list_int.append(int(ing))

    print("received ingredients_list from user:")

    self.send_response(200)
    self.send_header('Access-Control-Allow-Origin', '*')
    self.send_header('Content-Type', 'application/json')
    self.end_headers()

    ##ALGORITHM function: find a recipe: pull from db
    recipe = algorithm.choose_recipe(ing_list_int)
    for r in recipe:
        print(r)
    print(type(recipe))

    #no "score" parameter on DB
    # recipe = {
    #      "recipe_name": "Cake",
    #      "picture_url": "C:\pictures\1.jpg",
    #      "score": 95,
    #      "ingredients": [
    #             {
    #                 "_id": 1,
    #                 "name": "tomato",
    #                 "amount": "2 units"
    #             },
    #             {
    #                 "_id": 2,
    #                 "name": "oil",
    #                 "amount": "1 cup"
    #             }
    #      ],
    #      "DIRECTIONS": [
    #          "step 1",
    #          "step 2",
    #          "step 3"
    #         ]
    # }

    self.wfile.write(json.dumps(recipe).encode('utf-8')) #on client side need to decode: json_from_server.decode('utf_8')
    print("sent json")

