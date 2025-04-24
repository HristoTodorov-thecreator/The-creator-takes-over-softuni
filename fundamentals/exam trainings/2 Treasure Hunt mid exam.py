chest = input().split('|')


while True:
    commands = input()
    if commands == 'Yohoho!':
        break
    splitted = commands.split()

    firstcom = splitted[0]
    if firstcom == 'Loot':
        items = splitted[1:]
        for item in items:
            if item not in chest:
                chest.insert(0,item)


    if firstcom == 'Drop':
        index_ = int(splitted[1])
        if index_ < len(chest):
            g = chest.pop(index_)
            chest.append(g)



    if firstcom == 'Steal':
        count = int(splitted[1])
        if count > len(chest):
            count = len(chest)
        last = chest[-count:]
        for s in range(count):
            chest.pop(-1)

        print(", ".join(last))
if len(chest) <=0:
    print(f"Failed treasure hunt.")

else:
    counted_items = len(chest)
    sum_char_len = 0

    for l in chest:
        length = len(l)
        sum_char_len += length


    result = sum_char_len / counted_items
    print(f"Average treasure gain: {result:.2f} pirate credits.")

