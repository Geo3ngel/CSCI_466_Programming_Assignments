import sys
import socket

def initDo():
    port = sys.argv[1:]
    fileName = sys.argv[2:]

"""import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")

r1 = conn.getresponse()

print(r1.status, r1.reason)

data1 = r1.read()  # This will return entire content.
# The following example demonstrates reading data in chunks.

conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.read(200)) #200 bytes"""
