# This file will serve as a means of testing communication over http
# Created by: George Engel, Beau Anderson , &
# 9/12/2018

from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO
import cgi
import urllib

global status
global html

status = [0]

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()



    def do_HEAD(self):
        self._set_headers()

    # Handles get requests to Server
    def do_GET(self):
        # These two lines are mandatory for the http request to be considered valid
        self.send_response(200)
        self.end_headers()

        # Writes message on web page
        # Also b makes the string bytes, hence why it dosen't error out
        # TODO: Make wfile actually take in the map file/another html file to format the page

        global html

        #the form action with the POST method makes the page refresh (calls python POST method)
        html = b"""<html>
        <style>
.btn-group button {
    background-color: #4CAF50; /* Green background */
    border: 1px solid green; /* Green border */
    color: white; /* White text */
    padding: 10px 24px; /* Some padding */
    cursor: pointer; /* Pointer/hand icon */
    float: left; /* Float the buttons side by side */
}

/* Clear floats (clearfix hack) */
.btn-group:after {
    content: "";
    clear: both;
    display: table;
}

.btn-group button:not(:last-child) {
    border-right: none; /* Prevent double borders */
}

/* Add a background color on hover */
.btn-group button:hover {
    background-color: #3e8e41;
}
</style>
        <head>
        <title>~Battle Ship~</title>
        </head>
        <body>
        <font size="20"> </font>
        <p> <font size="20">  <b>Battle Ship</b> </font>  </p>
        </body>
        
        <form action="server.py" method="testPrint">
            <div class="btn-group"
                style="width:100%">
                    <button name="pos" value='0' style=width:50%">0,0</button>
                    <button name="pos" value='1' style=width:50%">1,0</button>
                    <button name="pos" value='2' style=width:50%">2,0</button>
                    <button name="pos" value='3' style=width:50%">3,0</button>
                    <button name="pos" value='4' style=width:50%">4,0</button>
                    <button name="pos" value='5' style=width:50%">5,0</button>
                    <button name="pos" value='6' style=width:50%">6,0</button>
                    <button name="pos" value='7' style=width:50%">7,0</button>
                    <button name="pos" value='8' style=width:50%">8,0</button>
                    <button name="pos" value='9' style=width:50%">9,0</button>
                </div>
            </form>
        <form action="server.py" method="testPrint">
            <div class="btn-group"
                style="width:100%">
                    <button name="pos" value='0' style=width:50%">0,1</button>
                    <button name="pos" value='1' style=width:50%">1,1</button>
                    <button name="pos" value='2' style=width:50%">2,1</button>
                    <button name="pos" value='3' style=width:50%">3,1</button>
                    <button name="pos" value='4' style=width:50%">4,1</button>
                    <button name="pos" value='5' style=width:50%">5,1</button>
                    <button name="pos" value='6' style=width:50%">6,1</button>
                    <button name="pos" value='7' style=width:50%">7,1</button>
                    <button name="pos" value='8' style=width:50%">8,1</button>
                    <button name="pos" value='9' style=width:50%">9,1</button>
                </div>
            </form>
        <form action="server.py" method="testPrint">
            <div class="btn-group"
                style="width:100%">
                    <button name="pos" value='0' style=width:50%">0,2</button>
                    <button name="pos" value='1' style=width:50%">1,2</button>
                    <button name="pos" value='2' style=width:50%">2,2</button>
                    <button name="pos" value='3' style=width:50%">3,2</button>
                    <button name="pos" value='4' style=width:50%">4,2</button>
                    <button name="pos" value='5' style=width:50%">5,2</button>
                    <button name="pos" value='6' style=width:50%">6,2</button>
                    <button name="pos" value='7' style=width:50%">7,2</button>
                    <button name="pos" value='8' style=width:50%">8,2</button>
                    <button name="pos" value='9' style=width:50%">9,2</button>
                </div>
            </form>
        <form action="server.py" method="testPrint">
            <div class="btn-group"
                style="width:100%">
                    <button name="pos" value='0' style=width:50%">0,3</button>
                    <button name="pos" value='1' style=width:50%">1,3</button>
                    <button name="pos" value='2' style=width:50%">2,3</button>
                    <button name="pos" value='3' style=width:50%">3,3</button>
                    <button name="pos" value='4' style=width:50%">4,3</button>
                    <button name="pos" value='5' style=width:50%">5,3</button>
                    <button name="pos" value='6' style=width:50%">6,3</button>
                    <button name="pos" value='7' style=width:50%">7,3</button>
                    <button name="pos" value='8' style=width:50%">8,3</button>
                    <button name="pos" value='9' style=width:50%">9,3</button>
                </div>
            </form>
            <form action="server.py" method="testPrint">
            <div class="btn-group"
                style="width:100%">
                    <button name="pos" value='X0 Y4' style=width:50%">0,4</button>
                    <button name="pos" value='X1 Y4' style=width:50%">1,4</button>
                    <button name="pos" value='X2 Y4' style=width:50%">2,4</button>
                    <button name="pos" value='X3 Y4' style=width:50%">3,4</button>
                    <button name="pos" value='X4 Y4' style=width:50%">4,4</button>
                    <button name="pos" value='X5 Y4' style=width:50%">5,4</button>
                    <button name="pos" value='X6 Y4' style=width:50%">6,4</button>
                    <button name="pos" value='X7 Y4' style=width:50%">7,4</button>
                    <button name="pos" value='X8 Y4' style=width:50%">8,4</button>
                    <button name="pos" value='X9 Y4' style=width:50%">9,4</button>
                </div>
            </form>
            <form action="server.py" method="testPrint">
            <div class="btn-group"
                style="width:100%">
                    <button name="pos" value='0' style=width:50%">0,5</button>
                    <button name="pos" value='1' style=width:50%">1,5</button>
                    <button name="pos" value='2' style=width:50%">2,5</button>
                    <button name="pos" value='3' style=width:50%">3,5</button>
                    <button name="pos" value='4' style=width:50%">4,5</button>
                    <button name="pos" value='5' style=width:50%">5,5</button>
                    <button name="pos" value='6' style=width:50%">6,5</button>
                    <button name="pos" value='7' style=width:50%">7,5</button>
                    <button name="pos" value='8' style=width:50%">8,5</button>
                    <button name="pos" value='9' style=width:50%">9,5</button>
                </div>
            </form>
        <form action="server.py" method="testPrint">
            <div class="btn-group"
                style="width:100%">
                    <button name="pos" value='0' style=width:50%">0,1</button>
                    <button name="pos" value='1' style=width:50%">1,1</button>
                    <button name="pos" value='2' style=width:50%">2,1</button>
                    <button name="pos" value='3' style=width:50%">3,1</button>
                    <button name="pos" value='4' style=width:50%">4,1</button>
                    <button name="pos" value='5' style=width:50%">5,1</button>
                    <button name="pos" value='6' style=width:50%">6,1</button>
                    <button name="pos" value='7' style=width:50%">7,1</button>
                    <button name="pos" value='8' style=width:50%">8,1</button>
                    <button name="pos" value='9' style=width:50%">9,1</button>
                </div>
            </form>
        <form action="server.py" method="testPrint">
            <div class="btn-group"
                style="width:100%">
                    <button name="pos" value='0' style=width:50%">0,2</button>
                    <button name="pos" value='1' style=width:50%">1,2</button>
                    <button name="pos" value='2' style=width:50%">2,2</button>
                    <button name="pos" value='3' style=width:50%">3,2</button>
                    <button name="pos" value='4' style=width:50%">4,2</button>
                    <button name="pos" value='5' style=width:50%">5,2</button>
                    <button name="pos" value='6' style=width:50%">6,2</button>
                    <button name="pos" value='7' style=width:50%">7,2</button>
                    <button name="pos" value='8' style=width:50%">8,2</button>
                    <button name="pos" value='9' style=width:50%">9,2</button>
                </div>
            </form>
        <form action="server.py" method="testPrint">
            <div class="btn-group"
                style="width:100%">
                    <button name="pos" value='0' style=width:50%">0,3</button>
                    <button name="pos" value='1' style=width:50%">1,3</button>
                    <button name="pos" value='2' style=width:50%">2,3</button>
                    <button name="pos" value='3' style=width:50%">3,3</button>
                    <button name="pos" value='4' style=width:50%">4,3</button>
                    <button name="pos" value='5' style=width:50%">5,3</button>
                    <button name="pos" value='6' style=width:50%">6,3</button>
                    <button name="pos" value='7' style=width:50%">7,3</button>
                    <button name="pos" value='8' style=width:50%">8,3</button>
                    <button name="pos" value='9' style=width:50%">9,3</button>
                </div>
            </form>
            <form action="server.py" method="testPrint">
            <div class="btn-group"
                style="width:100%">
                    <button name="pos" value='0,4' style=width:50%">0,4</button>
                    <button name="pos" value='1,4' style=width:50%">1,4</button>
                    <button name="pos" value='2,4' style=width:50%">2,4</button>
                    <button name="pos" value='3,4' style=width:50%">3,4</button>
                    <button name="pos" value='4,4' style=width:50%">4,4</button>
                    <button name="pos" value='5,4' style=width:50%">5,4</button>
                    <button name="pos" value='6,4' style=width:50%">6,4</button>
                    <button name="pos" value='7,4' style=width:50%">7,4</button>
                    <button name="pos" value='8,4' style=width:50%">8,4</button>
                    <button name="pos" value='9/,4' style=width:50%">9,4</button>
                </div>
            </form>
            
        <form action="server.py" method="testPrint">
    	    <p> <button name='bang' value ='0'  type="submit1">Bang</button> </p>
            <p> <button name='Boom' value ='1' type="submit2">Boom</button> </p>
            <p> <button name='Boomer' value ='2' type="submit3">Boomer</button> </p>
            <p> <button name='Boomest' value ='3' type="submit4">Boomest</button> </p>
            <p> <button name='Surrender Like a Coward' value ='4' type="submit5">Surrender like a coward</button> </p>
            <p> <button name='Cheetos' value ='5' type="submit6">Clever button name here</button> </p>
        </form>
            
        <form action="server.py" method="testPrint">
            <p> <button name='pythonB' value ='5' type="submit7">PythonTest</button> </p>
        </form>
        </html>"""

        #form = cgi.FieldStorage()
        #searchterm = form.getvalue('pythonB')

        #print(searchterm)

        #TODO: Use urllib to get current path & parse it into shots fired, process, and respond
        self.wfile.write(html)

    def testPrint(self):
        print("button called python code")



    #Have board modification logic here?
    #Add each row one at a time and manipulate in html?
    def do_POST(self):
        global html
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        #Posts the message below to webpage
        response.write(b'This is POST request. ')
        response.write(b'Received: ')
        response.write(body)
        #use response.getvalue() instead of html for text
        #TODO: make use of editable file instead of html?
        self.wfile.write(html)
        print("posted")

    def process_post_header(self):
        # get the referer
        referer = self.headers.get('Referer')
        # if visited from ui.html, redirect to referer URI
        if referer.endswith('ui.html'):
            self.send_response(301)
            self.send_header('Location', referer)
        else:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(self.html)

# Sets up the server
httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()
