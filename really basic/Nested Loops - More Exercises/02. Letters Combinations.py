start = input()
end = input()
expaction = input()

comb = 0

for x in range (ord(start), ord(end) +1):
    if x == ord(expaction):
        continue
    for y in range (ord(start), ord(end)+ 1):
        if y == ord(expaction):
            continue
        for z in range(ord(start), ord(end)+ 1):
            if z == ord(expaction):
                continue
            comb += 1
            print(f'{chr(x)}{chr(y)}{chr(z)}' ,end=  " " )
print(comb)