number = int(input())

plantst = {}
secondplants_rarity = {}
counter = {}

for i in range(number):
    splitted = input().split('<->')
    theplant = splitted[0]
    rarity = int(splitted[1])

    if theplant not in plantst:
        plantst[theplant] = {'rarity': rarity,'rating': []}




while True:
    command = input()

    if command == 'Exhibition':
        break

    second_split = command.split(': ')
    action = second_split[0]
    details = second_split[1]




    if action == 'Rate':
        plant, number = details.split(' - ')
        number = int(number)


        if plant in plantst:
            plantst[plant]['rating'].append(int(number))





        else:
            print(f'error')


    if action == 'Update':
        plant, number = details.split(' - ')
        number = int(number)
        if plant in plantst:
             plantst[plant]['rarity'] = number
        else:
            print(f'error')

    if action == 'Reset':
        tsplit = details.split(' - ')
        plant = tsplit[0]
        if plant in plantst:


            plantst[plant]['rating'] = []
        else:
            print(f'error')


print(f'Plants for the exhibition:')

for t in plantst:
    rare = plantst[t]['rarity']
    ratings = plantst[t]['rating']



    if not plantst[t]['rating']:

        print(f'- {t}; Rarity: {rare}; Rating: 0.00')
    else:
        avarage = sum(ratings) / len(ratings)
        print(f'- {t}; Rarity: {rare}; Rating: {avarage:.2f}')





