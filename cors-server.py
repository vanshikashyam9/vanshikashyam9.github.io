# save as serve_cors.py and run: python3 serve_cors.py
from http.server import HTTPServer, SimpleHTTPRequestHandler

class CORSRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, Range")
        super().end_headers()
    def do_OPTIONS(self):
        self.send_response(204)
        self.end_headers()

if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 8000), CORSRequestHandler).serve_forever()
