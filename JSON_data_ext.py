#Extract ('comment_counts') from the provided JSON file and compute the sum
import urllib.request, urllib.parse
import json

#request user input, else proceed
url = input('Enter url or press enter to continue:')
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_2239507.json'
print('Retrieving:', url)

try:
    host = urllib.request.urlopen(url)
    data = host.read()
    #Parse the data from the JSON file, output data
    info = json.loads(data)
    print('User Info:', len(info), info)

except:
    print('No User Info')
    exit()

#Identify which JSON list the required item is located in
item_location = info['comments']
print('Comments List:', info['comments'])

counts = list()

#Extract data from JSON list and append
for item in info['comments']:
    value = int(item['count'])
    counts.append(value)

print('Counts:' , counts)
print('Count of Counts:', len(counts))
print('Sum:', sum(counts))

