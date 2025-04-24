
year = int(input())
while True:
    year+= 1
    yearstr = str(year)
    if len(set(yearstr)) == len(yearstr):
        break

print(year)