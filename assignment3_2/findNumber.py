fileName=input('input the name of the file\n')
file=open(fileName)
handle=file.read()
import re
numbers=re.findall('[0-9]+',handle)
sum=0
for word in numbers:
    number=float(word)
    sum=sum+number
print("sum="+str(sum))
