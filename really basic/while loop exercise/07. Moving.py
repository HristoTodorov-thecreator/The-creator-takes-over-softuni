total = int(input()) * int(input()) * int(input())
freespace = 0
while total >= freespace:
    g = input()
    if g == 'Done':
        print(f'{total - freespace} Cubic meters left.')
        break

    freespace += int(g)

else:
    print(f'No more free space! You need {abs(total - freespace)} Cubic meters more.')
