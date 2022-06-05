from http.server import BaseHTTPRequestHandler
from urllib import parse
import platform

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
        s = self.path
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)

        message = 'Hello to Calculator\n\n\n'

        operation = dic.get('operation')
        first = dic.get('first')
        second = dic.get('second')

        if operation:
            message += f'{operation.capitalize()} Operation\n\n'
            if operation == "add":
                message += f'result of {operation.capitalize()} {first} to {second} is {first + second}'
            elif operation == "minus":
                message += f'result of {operation.capitalize()} {first} from {second} is {first - second}'
            else:
                message += 'Operation is unrecognized'
        else:
            message += 'enter in url operation value of add OR minus, and first as integer or float value, second as integer as float value'

        message += '\n\nYou may find me @ https://Suhaib.dev'
        
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(message.encode())