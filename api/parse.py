from http.server import BaseHTTPRequestHandler
from urllib import parse
import platform

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
        s = self.path
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)

        name = dic.get('name')
        if name:
            message = f'Hello {name}'
        else:
            message = 'Hello stranger'
        
        message += f'\nHello from {platform.node()}'
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(message.encode())