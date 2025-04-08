start = input()
end = input()
string  = input()

start = ord(start)
end =  ord(end)

listed = []
for n in range(start + 1,end):
    listed.append(chr(n))



total = 0
for i in string:
    if i in listed:
        total += ord(i)

print(total)
