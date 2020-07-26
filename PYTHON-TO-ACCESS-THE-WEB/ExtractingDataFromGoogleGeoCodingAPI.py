import urllib.request
import urllib.parse
import urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/json?"
address = input('Enter location: ')
params = dict()
params['key'] = 42
params['address'] = address
url = url + urllib.parse.urlencode(params)
print("Retrieving", url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')
info = json.loads(data)

place_id = info["results"][0].get("place_id", None)
print("Place id", place_id)
