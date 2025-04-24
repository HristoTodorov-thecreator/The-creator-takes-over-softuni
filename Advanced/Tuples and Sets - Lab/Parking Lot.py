number_of_cars = int(input())

g= set()
for i in range(number_of_cars):
    out_or_in,car = input().split(', ')

    if out_or_in == 'IN':
        g.add(car)
    elif out_or_in == 'OUT':
        g.remove(car)



if g:

    for n in g:
        print(n)
else:
    print(f'Parking Lot is Empty')