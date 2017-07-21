# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 22:22:12 2017

@author: AnthyG
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
"""
Very simple HTTP server in python.
Usage::
    ./dummy-web-server.py [<port>]
Send a GET request::
    curl http://localhost
Send a HEAD request::
    curl -I http://localhost
Send a POST request::
    curl -d "foo=bar&bin=baz" http://localhost
"""

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        
        p = self.path + "<br />" + self.requestline + "<br />" + self.address_string()
        
        sendstring = "<html><body><p>"+p+"</p></body></html>"
        self.wfile.write(sendstring.encode())

    def do_HEAD(self):
        self._set_headers()
        
    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = str(self.rfile.read(content_length).decode()) # <--- Gets the data itself
        
        self._set_headers()
        
        p = self.path + "<br />" + self.requestline + "<br />" + self.address_string()
        
        sendstring = "<html><body><p>"+p+"</p><p>"+post_data+"</p></body></html>"
        self.wfile.write(sendstring.encode())
        
def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('127.0.0.1', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd on port ' + str(port))
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    print("starting interface")
    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()