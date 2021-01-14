__author__ = 'mmalca'

from http.server import BaseHTTPRequestHandler, HTTPServer
##import json
from http_server.server_http_handler import httpHandler


def init_server():
    PORT = 80
    IP = '10.10.248.98'
    ##server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server = HTTPServer((IP , PORT), httpHandler)
    print('Server is running on port %s'%PORT)
    server.serve_forever()

init_server()