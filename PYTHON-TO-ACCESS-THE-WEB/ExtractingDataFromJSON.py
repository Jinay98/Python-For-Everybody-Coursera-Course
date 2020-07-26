import urllib.request
import urllib.parse
import urllib.error
import json
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')
print("Retrieving", address)
uh = urllib.request.urlopen(address, context=ctx)
data = uh.read()
print('Retrieved', len(data), 'characters')
info = json.loads(data.decode())
comments = info.get('comments', None)
sum = 0
count = 0
if comments:
    for comment in comments:
        count += 1
        sum += int(comment.get('count'))
print("Count:", count)
print("Sum:", sum)
