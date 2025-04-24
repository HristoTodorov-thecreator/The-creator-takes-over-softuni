

cities = {}

while True:
    command = input()
    if command == 'Sail':
        break
    spllitted = command.split('||')

    city = spllitted[0]
    thepop = int(spllitted[1])
    thegold = int(spllitted[2])
    if spllitted[0] in cities:
        cities[city]['population'] += thepop
        cities[city]['gold'] += thegold


    else:
        cities[city] = {'population':thepop,'gold':thegold}


while True:
    secondcommand = input()
    secondsplit = secondcommand.split('=>')


    if secondcommand == 'End':
        break

    plunder_or_prospher = secondsplit[0]

    if plunder_or_prospher == 'Plunder':
        thecity = secondsplit[1]
        thepeople = int(secondsplit[2])
        thegold = int(secondsplit[3])
        cities[thecity]['population'] -= thepeople
        cities[thecity]['gold'] -= thegold
        print(f"{thecity} plundered! {thegold} gold stolen, {thepeople} citizens killed.")
        if cities[thecity]['population'] == 0 or cities[thecity]['gold'] ==0:
            print(f"{thecity} has been wiped off the map!")
            del cities[thecity]


    if plunder_or_prospher == 'Prosper':
        thecity = secondsplit[1]
        thegold = int(secondsplit[2])
        if thegold <0:
            print(f"Gold added cannot be a negative number!" )
            continue
        else:
            cities[thecity]['gold'] += thegold
            total = cities[thecity]['gold']
            print(f'{thegold} gold added to the city treasury. {thecity} now has {total} gold.')



if len(cities) >0:
    print(f'Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:')
    for i in cities:
       thee = cities[i]['population']
       thesec = cities[i]['gold']
       print(f'{i} -> Population: {thee} citizens, Gold: {thesec} kg')

else:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")

