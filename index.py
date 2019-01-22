from http.server import BaseHTTPRequestHandler
import datetime, platform, sys


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        executables = [
            'datetime.datetime.now()',
            'datetime.datetime.utcnow()',
            'sys.version',
        ]
        for executable in executables:
            print(f'Evaluating {executable}')
            message = f'{executable} = {eval(executable)}\n'
            self.wfile.write(message.encode())
