# This file will serve as a means of testing communication over http
# Created by: George Engel, Beau Anderson , &
# 9/12/2018

from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO
import cgi
import urllib
from urllib.parse import urlparse

from urllib.request import urlopen
from urllib.parse import urlparse
import re
import BattleshipGame
import BattleshipGame
global status
global html
global req
global url



status = [0]

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    import BattleshipGame
    #replace with file parameter later
    file = None
    battleShipGame = BattleshipGame.BattleshipGame(file)

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

        filecontentA = ""
        filenameA = "own_board.txt"
        fileA = open(filenameA, "r")
        for line in fileA:
            filecontentA += "<p>"+line+"</p>"
        fileA.close()

        filecontentB = ""
        filenameB = "opponent_board.txt"
        fileB = open(filenameB, "r")
        for line in fileB:
            filecontentB += "<p>" + line + "</p>"
        fileB.close()
        #the form action with the POST method makes the page refresh (calls python POST method)
        html = bytes("""<html>
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

function myFunction(){   
    var colors = ["green", "black","yellow"],
    selectedColor = colors[Math.floor(Math.random()*colors.length)]
    $("body").css("background-color", selectedColor);
}


</style>
        <head>
        <title>~Battle Ship~</title>
        </head>
        <body>
        <font size="20"> </font>
        <p> <font size="20">  <b>Battle Ship</b> </font>  </p>
        </body>
        
        <form action="server.py" method="">
            <div class="btn-group"
                style="width:100%">
                    """ + filecontentA + "\n\n"+filecontentB+"""
                    
                </div>
            </form>

    
        <form action="server.py" method="get">
            <div class="btn-group"
                style="width:100%">
            
                    
                    <button name="pos" value='X0 Y0' onclick="document.body.style.backgroundColor = 'blue';" style=width:50%">0,0</button>
                    <button name="pos" value='X1 Y0' style=width:50%">1,0</button>
                    <button name="pos" value='X2 Y0' style=width:50%">2,0</button>
                    <button name="pos" value='X3 Y0' style=width:50%">3,0</button>
                    <button name="pos" value='X4 Y0' style=width:50%">4,0</button>
                    <button name="pos" value='X5 Y0' style=width:50%">5,0</button>
                    <button name="pos" value='X6 Y0' style=width:50%">6,0</button>
                    <button name="pos" value='X7 Y0' style=width:50%">7,0</button>
                    <button name="pos" value='X8 Y0' style=width:50%">8,0</button>
                    <button name="pos" value='X9 Y0' style=width:50%">9,0</button>
                </div>
            </form>
        <form action="server.py" method="get">
            <div class="btn-group"
                style="width:100%">
                    <button name="pos" value='X0 Y1' style=width:50%">0,1</button>
                    <button name="pos" value='X1 Y1' style=width:50%">1,1</button>
                    <button name="pos" value='X2 Y1' style=width:50%">2,1</button>
                    <button name="pos" value='X3 Y1' style=width:50%">3,1</button>
                    <button name="pos" value='X4 Y1' style=width:50%">4,1</button>
                    <button name="pos" value='X5 Y1' style=width:50%">5,1</button>
                    <button name="pos" value='X6 Y1' style=width:50%">6,1</button>
                    <button name="pos" value='X7 Y1' style=width:50%">7,1</button>
                    <button name="pos" value='X8 Y1' style=width:50%">8,1</button>
                    <button name="pos" value='X9 Y1' style=width:50%">9,1</button>
                </div>
            </form>
        <form action="server.py" method="get">
            <div class="btn-group"
                style="width:100%">
                    <button name="pos" value='X0 Y2' style=width:50%">0,2</button>
                    <button name="pos" value='X1 Y2' style=width:50%">1,2</button>
                    <button name="pos" value='X2 Y2' style=width:50%">2,2</button>
                    <button name="pos" value='X3 Y2' style=width:50%">3,2</button>
                    <button name="pos" value='X4 Y2' style=width:50%">4,2</button>
                    <button name="pos" value='X5 Y2' style=width:50%">5,2</button>
                    <button name="pos" value='X6 Y2' style=width:50%">6,2</button>
                    <button name="pos" value='X7 Y2' style=width:50%">7,2</button>
                    <button name="pos" value='X8 Y2' style=width:50%">8,2</button>
                    <button name="pos" value='X9 Y2' style=width:50%">9,2</button>
                </div>
            </form>
        <form action="server.py" method="get">
            <div class="btn-group"
                style="width:100%">
                    <button name="pos" value='X0 Y3' style=width:50%">0,3</button>
                    <button name="pos" value='X1 Y3' style=width:50%">1,3</button>
                    <button name="pos" value='X2 Y3' style=width:50%">2,3</button>
                    <button name="pos" value='X3 Y3' style=width:50%">3,3</button>
                    <button name="pos" value='X4 Y3' style=width:50%">4,3</button>
                    <button name="pos" value='X5 Y3' style=width:50%">5,3</button>
                    <button name="pos" value='X6 Y3' style=width:50%">6,3</button>
                    <button name="pos" value='X7 Y3' style=width:50%">7,3</button>
                    <button name="pos" value='X8 Y3' style=width:50%">8,3</button>
                    <button name="pos" value='X9 Y3' style=width:50%">9,3</button>
                </div>
            </form>
            <form action="server.py" method="get">
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
            <form action="server.py" method="get">
            <div class="btn-group"
                style="width:100%">
                    <button name="pos" value='X0 Y5' style=width:50%">0,5</button>
                    <button name="pos" value='X1 Y5' style=width:50%">1,5</button>
                    <button name="pos" value='X2 Y5' style=width:50%">2,5</button>
                    <button name="pos" value='X3 Y5' style=width:50%">3,5</button>
                    <button name="pos" value='X4 Y5' style=width:50%">4,5</button>
                    <button name="pos" value='X5 Y5' style=width:50%">5,5</button>
                    <button name="pos" value='X6 Y5' style=width:50%">6,5</button>
                    <button name="pos" value='X7 Y5' style=width:50%">7,5</button>
                    <button name="pos" value='X8 Y5' style=width:50%">8,5</button>
                    <button name="pos" value='X9 Y5' style=width:50%">9,5</button>
                </div>
            </form>
        <form action="server.py" method="get">
            <div class="btn-group"
                style="width:100%">
                    <button name="pos" value='X0 Y6' style=width:50%">0,6</button>
                    <button name="pos" value='X1 Y6' style=width:50%">1,6</button>
                    <button name="pos" value='X2 Y6' style=width:50%">2,6</button>
                    <button name="pos" value='X3 Y6' style=width:50%">3,6</button>
                    <button name="pos" value='X4 Y6' style=width:50%">4,6</button>
                    <button name="pos" value='X5 Y6' style=width:50%">5,6</button>
                    <button name="pos" value='X6 Y6' style=width:50%">6,6</button>
                    <button name="pos" value='X7 Y6' style=width:50%">7,6</button>
                    <button name="pos" value='X8 Y6' style=width:50%">8,6</button>
                    <button name="pos" value='X9 Y6' style=width:50%">9,6</button>
                </div>
            </form>
        <form action="server.py" method="get">
            <div class="btn-group"
                style="width:100%">
                    <button name="pos" value='X0 Y7' style=width:50%">0,7</button>
                    <button name="pos" value='X1 Y7' style=width:50%">1,7</button>
                    <button name="pos" value='X2 Y7' style=width:50%">2,7</button>
                    <button name="pos" value='X3 Y7' style=width:50%">3,7</button>
                    <button name="pos" value='X4 Y7' style=width:50%">4,7</button>
                    <button name="pos" value='X5 Y7' style=width:50%">5,7</button>
                    <button name="pos" value='X6 Y7' style=width:50%">6,7</button>
                    <button name="pos" value='X7 Y7' style=width:50%">7,7</button>
                    <button name="pos" value='X8 Y7' style=width:50%">8,7</button>
                    <button name="pos" value='X9 Y7' style=width:50%">9,7</button>
                </div>
            </form>
        <form action="server.py" method="get">
            <div class="btn-group"
                style="width:100%">
                    <button name="pos" value='X0 Y8' style=width:50%">0,8</button>
                    <button name="pos" value='X1 Y8' style=width:50%">1,8</button>
                    <button name="pos" value='X2 Y8' style=width:50%">2,8</button>
                    <button name="pos" value='X3 Y8' style=width:50%">3,8</button>
                    <button name="pos" value='X4 Y8' style=width:50%">4,8</button>
                    <button name="pos" value='X5 Y8' class="btn btn-default btn-primary style=width:50%">5,8</button>
                    <button name="pos" value='X6 Y8' style=width:50%">6,8</button>
                    <button name="pos" value='X7 Y8' style=width:50%">7,8</button>
                    <button name="pos" value='X8 Y8' style=width:50%">8,8</button>
                    <button name="pos" value='X9 Y8' style=width:50%">9,8</button>
                </div>
            </form>
            <form action="server.py" method="get">
            <div class="btn-group"
                style="width:100%">
                    <button name="pos" value='X0 Y9' style=width:50%">0,9</button>
                    <button name="pos" value='X1 Y9' style=width:50%">1,9</button>
                    <button name="pos" value='X2 Y9' style=width:50%">2,9</button>
                    <button name="pos" value='X3 Y9' style=width:50%">3,9</button>
                    <button name="pos" value='X4 Y9' style=width:50%">4,9</button>
                    <button name="pos" value='X5 Y9' style=width:50%">5,9</button>
                    <button name="pos" value='X6 Y9' style=width:50%">6,9</button>
                    <button name="pos" value='X7 Y9' style=width:50%">7,9</button>
                    <button name="pos" value='X8 Y9' style=width:50%">8,9</button>
                    <button name="pos" value='X9 Y9' style=width:50%">9,9</button>
                </div>
            </form>
            
        </html>""",'utf-8')

        #Breaks up the url query into coordinates if applicable
        #TODO: In the if statement, make a call to the other server on local host to check for these coords
        #into shots fired, process, and respond
        pattern = re.compile('X(\d*)\+Y(\d*)')

        p = pattern.search(self.path)
        if(p!= None):
            num1 = int(p.group(1))
            num2 = int(p.group(2))
            if((num1 >= 0 and num1 <= 9)and(num2 >= 0 and num2 <= 9)):
                print(num1," ",num2)
                self.battleShipGame.shoot(num1,num2)
                if(self.battleShipGame.checkWin()):
                    #TODO: Declare Winner
                    print("Game Over")
            else:
                self.send_response(404)

        self.wfile.write(html)

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

        print(self.path)

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
