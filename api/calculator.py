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
            if operation == "add":
                message += 'Add / Sum Operation\n\n'
                message += f'result of {operation.capitalize()} {first} to {second} is {float(first) + float(second)}'
            elif operation == "minus":
                message += 'Deduct / Minus Operation\n\n'
                message += f'result of {operation.capitalize()} {first} from {second} is {float(first) - float(second)}'
            else:
                message += 'Operation is unrecognized'
        else:
            message += 'To use calculator, enter in url operation value of add OR minus, and first as integer or float value, second as integer or float value'

        message += '\n\nYou may find me @ https://Suhaib.dev'
        
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(message.encode())