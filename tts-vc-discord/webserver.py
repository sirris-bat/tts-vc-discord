from http.server import BaseHTTPRequestHandler, HTTPServer
import socket
import os
from mimetypes import types_map

hostname = "localhost"
port = 4000

webdir = "../web"

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path == "/":
                self.path = "index.html"
            filename, ext = os.path.splitext(self.path)
            if ext in (".html", ".css", ".js"):
                with open(os.path.join(os.getcwd(), webdir, self.path.lstrip("/")), "rb") as file:
                    self.send_response(200)
                    self.send_header("Content-type", types_map[ext])
                    self.end_headers()
                    self.wfile.write(file.read())
                    file.close()
            return
        except IOError as e:
            self.send_error(404)

class TimeoutHTTPServer(HTTPServer):
    def get_request(self):
        self.socket.settimeout(10.0)
        result = None
        while result is None:
            try:
                result = self.socket.accept()
            except socket.timeout:
                pass
        result[0].settimeout(None)
        return result

def start_server():
    webserver = TimeoutHTTPServer((hostname, port), Handler)
    webserver.serve_forever()
