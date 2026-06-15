from http.server import BaseHTTPRequestHandler, HTTPServer


HOST = "0.0.0.0"
PORT = 8080


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self._send_response(200, "Hello from Effective Mobile!\n")
        elif self.path == "/health":
            self._send_response(200, "OK\n")
        else:
            self._send_response(404, "Not Found\n")

    def _send_response(self, status_code: int, body: str):
        response = body.encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(response)))
        self.end_headers()
        self.wfile.write(response)


if __name__ == "__main__":
    server = HTTPServer((HOST, PORT), RequestHandler)
    print(f"Backend server is running on {HOST}:{PORT}", flush=True)
    server.serve_forever()
