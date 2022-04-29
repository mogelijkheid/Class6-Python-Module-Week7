
fh = open('new1.txt')
count=0
x='India'
for line in fh:
    if x in line:
        count+=1
    else:
        continue
print  ("there are {} times {} in text".format(count,x))