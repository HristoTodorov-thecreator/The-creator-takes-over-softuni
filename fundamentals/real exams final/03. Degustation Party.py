
liked_meals = {}
unliked = 0
while True:
    command = input()
    if command == 'Stop':
        break
    splited = command.split('-')
    action = splited[0]
    if action == 'Like':
        guest = splited[1]
        meal = splited[2]
        if guest not in liked_meals:
            liked_meals[guest] = []

        if meal not in liked_meals[guest]:
            liked_meals[guest].append(meal)



    if action == 'Dislike':
        guest = splited[1]
        meal = splited[2]
        if guest in liked_meals:

            if meal in liked_meals[guest]:
                liked_meals[guest].remove(meal)
                print(f"{guest} doesn't like the {meal}.")

                unliked += 1

            else:
                print(f"{guest} doesn't have the {meal} in his/her collection.")

        else:
            print(f'{guest} is not at the party.')


for m in liked_meals:
    print(f'{m}: {", ".join(liked_meals[m])}')

print(f'Unliked meals: {unliked}')