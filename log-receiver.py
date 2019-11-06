#!/usr/bin/env python

from http.server import HTTPServer, BaseHTTPRequestHandler

class S(BaseHTTPRequestHandler):
    def _do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "application/x-www-form-urlencoded")
        self.end_headers()
        print("asd")
        
def run(server_class=HTTPServer, handler_class=S, addr, port):
    server_address = (addr, port)
    httpd = server_class(server_address, handler_class)
    print(f"Listening on {addr}:{port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run(addr="localhost", port=1337)
