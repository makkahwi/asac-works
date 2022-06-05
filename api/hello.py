from http.server import BaseHTTPRequestHandler


class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    #  request is successful and you will get your response
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    message = "Hello World War III"
    message += '\n\nThis is static page\n\nYou may find me @ https://Suhaib.dev'
    self.wfile.write(message.encode())
    return