print("Contenet-Type: index/html")


import cgi
form = cgi.FieldStorage()
Chemy = form["chemistry"]
Math = form["Mathematics"]

print(Chemy,Math)