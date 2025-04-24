coffee = 0


while True:
    what_work = input()
    if what_work == 'END':
        break

    if what_work == 'coding' or what_work == 'cat' or what_work == 'dog' or what_work == 'movie':
        coffee += 1
    if what_work == 'CODING' or what_work == 'CAT' or what_work == 'DOG' or what_work == 'MOVIE':
        coffee += 2
    else:
        continue
        

if coffee > 5:
    print(f'You need extra sleep')
else:
    print(f'{coffee}')