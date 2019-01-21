from http.server import BaseHTTPRequestHandler
from cowpy import cow
import sys

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        message = cow.Cowacter().milk('Hello from Python ' + str(sys.version))
        self.wfile.write(message.encode())
        return
