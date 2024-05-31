#!/usr/bin/python3
"""
    Module that set up basic HTTP Server
"""


from http.server import HTTPServer, BaseHTTPRequestHandler
import json


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    """
    Class that create a simple server
    """

    def do_GET(self):
        """
        Method that handle GET request"""
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Hello, this is a simple API!')
        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {
                'name': 'John Doe',
                'age': 30,
                'city': 'New York'
            }
            self.wfile.write(json.dumps(data).encode("utf-8"))
        elif self.path == '/info':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {
                'version': '1.0',
                'description': 'A simple API built with http.server'
            }
            self.wfile.write(json.dumps(data).encode("utf-8"))
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")
        else:
            self.send_error(404, 'Endpoint not found')


def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    """ Function that run the server """
    server_address = ('localhost', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == "__main__":
    """
        Main function that run the server
    """
    run()
