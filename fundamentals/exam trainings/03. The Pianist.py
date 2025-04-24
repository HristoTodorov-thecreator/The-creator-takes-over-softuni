collection = int(input())

alldata = {}


for i in range(collection):
    data = input().split('|')
    piece = data[0]
    composer = data[1]
    key = data[2]
    alldata[piece] = {'composer':composer,'key':key}

while True:
    command = input().split('|')




    action = command[0]
    if action == 'Stop':
        break


    if action == 'Add':
        newpiece = command[1]
        newcomposer = command[2]
        newkey = command[3]
        if newpiece not in alldata:
            alldata[newpiece] = {'composer':newcomposer,'key':newkey}
            print(f"{newpiece} by {newcomposer} in {newkey} added to the collection!")
        else:
            print(f"{newpiece} is already in the collection!")

    if action == 'Remove':
        removepiece = command[1]
        if removepiece in alldata:
            print(f'Successfully removed {removepiece}!')
            del alldata[removepiece]

        else:
            print(f"Invalid operation! {removepiece} does not exist in the collection.")
    if action == 'ChangeKey':
        changepiece = command[1]
        changekey = command[2]
        if changepiece in alldata:
            oldkey = alldata[changepiece]['key']
            print(f'Changed the key of {changepiece} to {changekey}!')
            alldata[changepiece]['key'] = changekey
        else:
            print(f"Invalid operation! {changepiece} does not exist in the collection.")

for s in alldata:
    thepiece = s
    thecomposer = alldata[s]['composer']
    thekey = alldata[s]['key']
    print(f"{thepiece} -> Composer: {thecomposer}, Key: {thekey}")

