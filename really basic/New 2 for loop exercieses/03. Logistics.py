g = int(input())


bus = 0
truck = 0
train = 0
busprice = 200
truckprice = 175
trainprice = 120


for i in range(g):
    tons = int(input())
    if 0 <= tons <= 3:
        bus += tons

    elif 4 <= tons <=11:
        truck += tons


    elif tons >= 12:
        train += tons


totaltons = bus + truck + train
total = bus * busprice + truck * truckprice + trainprice * train

average_cost_per_ton = total / totaltons

print(f'{average_cost_per_ton:.2f}')
print(f'{bus / totaltons * 100:.2f}%')
print(f'{truck / totaltons * 100:.2f}%')
print(f'{train / totaltons * 100:.2f}%')



