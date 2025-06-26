import urllib.request, urllib.parse
import ssl
import json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Prompt user for location
service_url = input('Enter Service URL: ')
#Continue to prompt until location has been entered
while True:
    location = input('Enter Location: ')
    if len(location) > 1:
        print('Please enter a valid location')
        break
#Strip whitespace and create a dictionary for storage of 'q parameters'
location = location.strip()
params = dict()
params ['q'] = location

api_url = service_url + urllib.parse.urlencode(params)
print('Retrieving:', api_url)

#Read the response data and decode into a string
host = urllib.request.urlopen(api_url,context=ctx)
data = host.read().decode()
#print('Received', len(data), 'characters',)

#Parse JSON data
json_data = json.loads(data)

#Data guardian
if not json_data or 'features' not in json_data:
    print('No features')
    print(data)

#print(json.dumps(json_data, indent=4))
#print(json.dumps(json_data['features'][0]['properties']['plus_code']))

plus_code = json_data['features'][0]['properties']['plus_code']
print("plus_code:", plus_code)