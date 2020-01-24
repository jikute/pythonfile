fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line = line.split()
    for i in range(len(line)-1):
        if line[i] in lst: continue
        else:
            lst.append(line[i])
print(lst.sort())
