# This file will serve as a means of testing communication over http
# Created by: George Engel, Beau Anderson , &
# 9/12/2018

from http.server import HTTPServer, BaseHTTPRequestHandler

global status
status = [0]

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    # Handles get requests to Server
    def do_GET(self):
        # These two lines are mandatory for the http request to be considered valid
        self.send_response(200)
        self.end_headers()

        # Writes message on web page
        # Also b makes the string bytes, hence why it dosen't error out
        # TODO: Make wfile actually take in the map file/another html file to format the page
        self.wfile.write(b"""<html>
<head>
<title>~Battle Ship~</title>
</head>
<body>
<font size="20"> </font>
<p> <font size="20">  <b>Battle Ship</b> </font>  </p>
</body>
<p> <button type="submit1">Bang</button> </p>
<p> <button type="submit2">Boom</button> </p>
<p> <button type="submit3">Boomer</button> </p>
<p> <button type="submit4">Boomest</button> </p>
<p> <button type="submit5">Surrender like a coward</button> </p>
<p> <button type="submit6">Clever button name here</button> </p>
</html>""")
    #TODO: Actually make buttons functional (may need flask)

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


# Sets up the server
httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()
