from http.server import BaseHTTPRequestHandler
import datetime, os, pathlib, platform, sys, threading


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        executables = [
            'datetime.datetime.now()',
            'datetime.datetime.utcnow()',
            'os.getlogin()',
            'os.getpid()',
            'os.uname()',
            'pathlib.Path().resolve()',
            'platform.linux_distribution()',
            'platform.node()',
            'platform.platform()',
            'platform.uname()',
            'sys.version',
            'threading.current_thread().name',
            'threading.get_ident()',
        ]
        for executable in executables:
            message = f'{executable}\n{eval(executable)}\n\n'
            self.wfile.write(message.encode())
