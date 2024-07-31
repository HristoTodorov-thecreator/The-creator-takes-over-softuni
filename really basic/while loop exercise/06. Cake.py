total_cakes = int(input()) * int(input())
pieces_eat = 0

while total_cakes >= pieces_eat:
    g = input()
    if g == 'STOP':
        print(f'{total_cakes - pieces_eat} pieces are left.')
        break

    pieces_eat += int(g)

else:
    print(f'No more cake left! You need {abs(total_cakes - pieces_eat)} pieces more.')

