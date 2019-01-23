from http.server import BaseHTTPRequestHandler

from kdnfeed.feed import feed


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/rss+xml; charset=UTF-8')  # Alt value: text/xml; charset=UTF-8
        self.end_headers()
        self.wfile.write(feed())
