import urllib.request as urllib
import re

response = urllib.urlopen('https://www.whatismyip.com')
text = response.read().decode('utf-8')

match = re.search('(Detailed information about IP address.*)"', text)
print(match.group())
print(match.group(1))
