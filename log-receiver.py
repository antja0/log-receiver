#!/usr/bin/env python

from http.server import HTTPServer, BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def do_POST(self):        
        print("asd")
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

if __name__ == "__main__":
    server_address = ("localhost", 1337)
    server = HTTPServer(server_address, Handler)
    
    try:
        print("Listening...")
        server.serve_forever()
    except KeyboardInterrupt:
        print("Shutting down...")
        server.socket.close()
