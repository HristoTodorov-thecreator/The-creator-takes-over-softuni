elements = input().split()

moves = 0


while True:
    numbers = input()
    if numbers == 'end':
        break

    g = numbers.split()
    moves += 1
    indexone = int(g[0])
    indextwo = int(g[1])
    if indexone == indextwo or indexone < 0 or indexone >= len(elements) or indextwo < 0 or indextwo >= len(elements) :
        mid_ind = len(elements) // 2
        elements.insert(mid_ind,f'-{moves}a')
        elements.insert(mid_ind, f'-{moves}a')
        print(f'Invalid input! Adding additional elements to the board')
        continue



    if elements[indexone] == elements[indextwo]:
        element = elements[indexone]
        print(f'Congrats! You have found matching elements - {element}!')
        elements.pop(max(indexone,indextwo))
        elements.pop(min(indexone,indextwo))

    else:



        print('Try again!')
    if len(elements) == 0:
        print(f'You have won in {moves} turns!')
        break







if len(elements) > 0:
    print(f'Sorry you lose :(')
    print(' '.join(elements))



