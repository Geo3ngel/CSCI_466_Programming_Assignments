import cgi
import cgitb

cgitb.enable(display=0, logdir="logdir/", format="html")

print("Content-Type: text/html")    # HTML is following
print()      # blank line, end of headers

print("<html>")
print("<body>")
print("<head><TITLE>CGI script output</TITLE></head>")
print("<H1>This is my first CGI script</H1>")
print("Hello, world!")

form = cgi.FieldStorage()
if form.getvalue("name"):
    name = form.getvalue("name")
    print('<h1> Hello '+name+'! Thanks for using my script!<h1><br />')
if form.getvalue("happy"):
    print("<p>Great!</p>")
if form.getvalue("sad"):
    print("<p> Thats nice.</p>")

    print ('<form method="post" action="hello.py">')
    print ('<p>Name: <input type="text" name="name"/></p>')
    print ('input type="checkbox" name="happy" /> Happy')
    print ('input type="checkbox" name="sad" /> Sad')
    print ('input type="submit" value="Submit" />')
    print("</form>")
print("</body>")
print("</html>")
#if "name" not in form or "addr" not in form:
#    print("<H1>Error</H1>")
#    print("Please fill in the name and addr fields")

#print("<p>name:", form["name"].value)
#print("<p>addr:", form["addr"].value)
