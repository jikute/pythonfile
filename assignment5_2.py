largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    try:
        num=int(num)
    except:
        print('Invalid input')
    if(largest>=num):
        largest=largest
    elif(largest<num):
        largest=num
    if(smallest<=num):
        smallest=smallest
    elif(smallest>num):
        smallest=num
print("Maximum", largest)
print("Minimum", smallest)
