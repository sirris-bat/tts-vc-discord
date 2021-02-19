from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import os
from mimetypes import types_map

hostname = "localhost"
port = 4000

webdir = "../web"

class WebHandler(BaseHTTPRequestHandler):
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

async def start_server():
    webserver = HTTPServer((hostname, port), WebHandler)
    webserver.serve_forever()
