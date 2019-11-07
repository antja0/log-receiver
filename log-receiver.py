#!/usr/bin/env python

from http.server import HTTPServer, BaseHTTPRequestHandler
from colorama import init, Fore, Style

init()

class Handler(BaseHTTPRequestHandler):
    def get_color(self, level):
        levelColors = {
            "DEBUG": Fore.WHITE,
            "WARN": Fore.YELLOW,
            "ERROR": Fore.RED,
            "FATAL": Fore.RED
        }
        return levelColors.get(level, "")

    def do_POST(self):
        receiveIp = self.address_string()

        content_length = int(self.headers['Content-Length'])
        postData = self.rfile.read(content_length).decode('utf-8')
        logVars = postData.split('|')

        logTime = logVars[0]
        logName = logVars[1]
        logLevel = logVars[2].upper()
        logMessage = logVars[3]

        colorCode = self.get_color(logLevel)
        
        print(f"{logTime} - {receiveIp} ({logName}): {colorCode}{logLevel} {logMessage} {Style.RESET_ALL}\n")
        
        self.send_response(200)

    def log_message(self, format, *args):
        return

if __name__ == "__main__":
    server_address = ('', 3000)
    server = HTTPServer(server_address, Handler)
    
    try:
        print("Listening...")
        server.serve_forever()
    except KeyboardInterrupt:
        print("Shutting down...")
        server.socket.close()
