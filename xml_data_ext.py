#Parse and extract comment counts from xml file
#Compute sum of numbers from file
import xml.etree.ElementTree as ET
import urllib.request

#Request user input / debug and lead to correct file if bypassing entry
url = input("Input url or press enter to continue:")
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_2239506.xml'
print('Retrieving', url)

#Open and read the requested file
host = urllib.request.urlopen(url)
data = host.read()
print('Retrieved', len(data), 'characters')

#Parse and extract the data from xml file / append list
tree = ET.fromstring(data)
counts = (tree.findall('.//count'))
lst= list()

for count in counts:
    value = int(count.text)
    lst.append(value)
    continue

#Provide the user with output from collected data
print('Count:', len(lst))
print('Sum:', sum(lst))


