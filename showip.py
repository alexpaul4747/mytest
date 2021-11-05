import urllib.request as urllib
import json

response = urllib.urlopen('https://api.myip.com')
print(json.load(response))
