text = input().split()

bakery = {}
for i in range(0,len(text),2):
    thekey = text[i]
    thevalue = text[i+1]
    bakery[thekey] = int(thevalue)

print(bakery,end=' ')