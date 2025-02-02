total_space = int(input())
total =  0
price = 0
while True:
    people = input()
    if people == 'Movie time!':
        print(f'There are {abs(total_space - total)} seats left in the cinema.')
        print(f'Cinema income - {price} lv.')
        break
    else:
        g = int(people)
        if total + g>= total_space:
            print(f'The cinema is full.')
            print(f'Cinema income - {price} lv.')
            break




        if g % 3 ==0:
            price =price + (g * 5) - 5
        else:
            price =price + g * 5



        total += g

