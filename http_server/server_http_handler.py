__author__ = 'mmalca'

##from http_server.server_implementations import *
from  http_server import server_implementations
## from  http_server.server_implementations import get_ingredients_list
## from  http_server.server_implementations import get_recipe
from http.server import BaseHTTPRequestHandler


class httpHandler(BaseHTTPRequestHandler): ## This class inherits from BaseHTTPRequestHandler

    def do_GET(self):
        print("received GET request")
        print(self.path.partition('?'))
        if self.path == '/getAvailableIngredients':
            print("/getAvailableIngredients")
            server_implementations.get_ingredients_list(self)


        if self.path.startswith("/getRecipe"):
            print("/getRecipe")
            server_implementations.get_recipe(self)

