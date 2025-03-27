from http.client import HTTPConnection
HTTPConnection.debuglevel = 1

import urllib.request

a_url = "https://www.w3schools.com/xml/note.xml"
#sempre retorna bytes e não strings
response = urllib.request.urlopen(a_url)
data = response.read()
print(response.headers.as_string())
print(data)
print(len(data))