from http.server import HTTPServer, BaseHTTPRequestHandler


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    #Handles get requests to Server
    def do_GET(self):
        #These two lines are mandatory for the http request to be considered valid
        self.send_response(200)
        self.end_headers()

        #Writes message on web page
        #Also b makes the string bytes, hence why it dosen't error out
        self.wfile.write(b'Hello, world!')

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        response.write(b'This is POST request. ')
        response.write(b'Received: ')
        response.write(body)
        self.wfile.write(response.getvalue())
        print("TEST")


#Sets up the server
httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()