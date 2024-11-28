import datetime

print("Content-Type: text/html")    # HTML is following
print()                             # blank line, end of headers

print("<html>")
print("<head>")
print("<title>Python CGI Script</title>")
print("</head>")
print("<body>")
print("<h1>Hello, world!</h1>")
print("<p>The current date and time are: " + str(datetime.datetime.now()) + "</p>")
print("</body>")
print("</html>")
