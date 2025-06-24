#Scrape Dr Chucks webpage for student scores and find the sum
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
#Ignore SSL Certificate errors with:
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Identify URL to scrape
url = ('https://py4e-data.dr-chuck.net/comments_2239504.html')
html = urllib.request.urlopen(url, context=ctx).read() #(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

#retrieve anchor tags
total = 0

tags = soup('span')
for tag in tags:
    #look at parts of tag
    print('Comments:' ,tag.contents[0])

#create an integer for string contents and find the total(sum)
    val = int(tag.contents[0])
    total = total + val

print('Sum of Comments:', total)




