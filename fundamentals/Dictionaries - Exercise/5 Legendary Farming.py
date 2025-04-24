items = {'shards':0,'fragments':0,'motes':0}

obt = False

while not obt:
    curr_items = input().split()
    for ind in range(0,len(curr_items),2):
        key = curr_items[ind + 1].lower()
        value = int(curr_items[ind])

        if key not in items:
            items[key] = 0
        items[key] += value
        if items['shards'] >=250:
            print(f'Shadowmourne obtained!')
            items['shards'] -= 250
            obt = True
        if items['fragments'] >=250:
            print(f'Valanyr obtained!')
            items['fragments'] -= 250
            obt = True
        if items['motes'] >=250:
            print(f'Dragonwrath obtained!')
            items['motes'] -= 250
            obt = True

        if obt:
            break

for i,m in items.items():
    print(f'{i}: {m}')
