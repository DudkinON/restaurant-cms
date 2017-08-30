# import threading
import http.server
# from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
from don.router.Router import Router
from settings import settings
from socketserver import ThreadingMixIn
from don.dependencies.bleach import clean


class ThreadHTTPServer(ThreadingMixIn, http.server.HTTPServer):
    "This is an HTTPServer that supports thread-based concurrency."


class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # send headers
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        if self.path == '/favicon.ico':
            pass
        else:
            run = Router(self.path, settings)

            data = run.run_action()

            self.wfile.write(data.encode())

    def do_POST(self):
        # 1. How long was the message? (Use the Content-Length header.)
        length = int(self.headers.get('Content-length', 0))
        # 2. Read the correct amount of data from the request.
        data = self.rfile.read(length).decode()
        # 3. Extract the "message" field from the request data.
        message = clean(parse_qs(data)['text'][0])
        print(message)
        # Send the "message" field back as the response.
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        if message:
            self.wfile.write(message.encode())

    def get_header(self, error):
        self.send_response(error)


def server(ip='127.0.0.1', port=8000):
    print('Server running on ip: {}, and port: {}'.format(ip, port))
    print('http://{}:{}'.format(ip, port))
    httpd = ThreadHTTPServer((ip, port), Handler)
    httpd.serve_forever()

if __name__ == '__main__':
    server()
else:
    server = server
