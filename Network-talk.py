#This file will serve as a means of testing communication over http
# Created by: George Engel, Beau Anderson , &
# 9/12/2018

import BaseHTTPServer, SimpleHTTPServer
import ssl

httpd = BaseHTTPServer.HTTPServer(('localhost', 4443), SimpleHTTPServer.SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket (httpd.socket, certfile='path/to/localhost.pem', server_side=True)
httpd.serve_forever()

print("Hello")
