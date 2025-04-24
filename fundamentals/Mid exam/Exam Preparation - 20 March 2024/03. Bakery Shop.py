
foods = []
number_of_food = []
sold = 0
while True:
    command = input().split()
    if command[0] == 'Complete':
        break
    if command[0] == 'Receive':
        if int(command[1]) > 0:
            if command[2] not in foods:
                foods.append(command[2])
                number_of_food.append(int(command[1]))
            else:
                index_ = foods.index(command[2])
                number_of_food.insert(index_,int(command[1]))



    elif command[0] == 'Sell':
        if command[2] not in foods:
            print(f'You do not have any {command[2]}.')
        if command[2] in foods:
            index__ = foods.index(command[2])
            quan = int(command[1])

            if int(command[1]) <= int(number_of_food[index__]):
                number_of_food[index__] -= quan
                print(f'You sold {int(command[1])} {command[2]}.')
                sold  += int(command[1])
                if number_of_food[index__] == 0:
                    number_of_food.pop(index__)
                    foods.pop(index__)
            else:
                print(f"There aren't enough {command[2]}. You sold the last {number_of_food[index__]} of them.")
                sold += number_of_food[index__]
                foods.pop(index__)
                number_of_food.pop(index__)

for i in range(len(foods)):
    print(f'{foods[i]}: {number_of_food[i]}')

print(f'All sold: {sold} goods')




