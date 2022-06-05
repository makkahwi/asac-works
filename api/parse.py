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
            message = 'Hello dear\n\n You may include your name in url so we print it here with key of name'

        message += f'\nHello from {platform.node()}'
        message += '\n\nThis is static page\n\nYou may find me @ https://Suhaib.dev'
        
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(message.encode())