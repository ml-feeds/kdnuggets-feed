from http.server import BaseHTTPRequestHandler
import datetime, os, pathlib, platform, sys


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        executables = [
            'datetime.datetime.now()',
            'datetime.datetime.utcnow()',
            'os.uname()',
            'pathlib.Path().resolve()',
            'platform.linux_distribution()',
            'platform.node()',
            'platform.platform()',
            'platform.uname()',
            'sys.version',
        ]
        for executable in executables:
            message = f'{executable}\n{eval(executable)}\n\n'
            self.wfile.write(message.encode())
