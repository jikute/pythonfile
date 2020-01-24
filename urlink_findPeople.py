from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
position = input('Enter Position: ')
position = int(position)-1
counts = input('Enter Counts: ')
counts =int(counts)

for number in range(counts):
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    url = tags[position].get('href', None)
    print(url)
