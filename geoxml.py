#The program prompts for a URL, read the XML data from that URL using urllib
#then parse and extract the comment counts from the XML data,
#compute the sum of the numbers in the file.
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location:\n')
    if len(address) < 1: break
    print('Retrieving:\n', address)
    uh = urllib.request.urlopen(address, context=ctx)
    data = uh.read()
    print('Retrieved', len(data), 'characters')
    #print(data.decode())

    commentinfo = ET.fromstring(data)
    comment = commentinfo.findall('comments/comment')
    print('comment count:',len(comment))

    sum = 0
    for item in comment:
        count=item.find('count').text
        count=float(count)
        sum = sum+count
    print('sum:', sum)
