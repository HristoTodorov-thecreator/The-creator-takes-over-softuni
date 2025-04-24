text = input().replace(' ','')

new = {}


for i in text:
    if i not in new:
        new[i] = 0
    new[i] += 1

for key,value in new.items():
    print(f'{key} -> {value}')