from http.server import SimpleHTTPRequestHandler, HTTPServer
import os

class CustomHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

if __name__ == "__main__":
    os.chdir('./frontend/puzzle-8-game/public')  # Change directory to where the built files are
    port = 8000  # You can choose any port you like
    httpd = HTTPServer(('', port), CustomHandler)
    print(f"Serving on port {port}...")
    httpd.serve_forever()
