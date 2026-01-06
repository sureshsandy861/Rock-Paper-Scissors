import http.server
import socketserver
import json
from urllib.parse import urlparse, parse_qs
import game_logic  # Import the game logic

PORT = 8000

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        """Serve the HTML file or handle API requests."""
        if self.path.startswith("/play"):
            self.handle_game_request()
        else:
            self.path = "index.html"  # Serve the HTML file
            return http.server.SimpleHTTPRequestHandler.do_GET(self)

    def handle_game_request(self):
        """Handle game logic based on user input."""
        query = urlparse(self.path).query
        params = parse_qs(query)
        user_choice = params.get("choice", [""])[0]

        if user_choice not in ["rock", "paper", "scissors"]:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"Invalid choice")
            return

        # Get game result
        result = game_logic.play_game(user_choice)

        # Send JSON response
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(result).encode())

# Start the server
class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True

with ReusableTCPServer(("", PORT), MyHandler) as httpd:
    try:
        print(f"Serving at port {PORT}")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped by user")
        httpd.shutdown()
