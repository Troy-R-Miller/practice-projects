#extract href= values from user URL
#scan for a tag in a particular position and cycle through the link 'x' amount of times
#idenify the name in the final link
#link used for program has internal links that change positions (find position 18, cycle 7 times)
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Request user inputs
url = ('https://py4e-data.dr-chuck.net/known_by_Caoimhe.html')
cycle = int(input("Enter count: "))
position = int(input("Enter position: "))

print('Retrieving:' , url)

#follow links and collect page content
for links in range(cycle):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
#collect anchor tags
    tags = soup('a')
#set variable parameters
    pcount = 0
#read through each tag and add to position count
    for tag in tags:
        pcount = pcount + 1
        if pcount == position: #program is complete when position count reaches user specified 'position'
            print('Retrieving:' , tag.get('href',))
            url = tag.get('href',)
            #reset position count
            pcount = 0
            break
#identify final name search
print('Final name:' ,url)