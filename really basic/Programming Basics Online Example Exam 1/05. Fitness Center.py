visitors = int(input())

backtotal = 0
totalchest = 0
totallegs = 0
totalabs = 0
proteinshaketotal = 0
totalproteinb = 0
forworking = 0
forbuying = 0


for i in range (visitors):
    whathappened = input()
    if whathappened == 'Back':
        backtotal += 1
        forworking += 1
    elif whathappened == 'Chest':
        totalchest += 1
        forworking += 1
    elif whathappened == "Legs":
        totallegs += 1
        forworking += 1
    elif whathappened == 'Abs':
        totalabs += 1
        forworking += 1
    elif whathappened == 'Protein shake':
        proteinshaketotal += 1
        forbuying += 1
    elif whathappened == 'Protein bar':
        totalproteinb += 1
        forbuying += 1


print(f'{backtotal} - back')
print(f'{totalchest} - chest')
print(f'{totallegs} - legs')
print(f'{totalabs} - abs')
print(f'{proteinshaketotal} - protein shake')
print(f'{totalproteinb} - protein bar')
print(f'{forworking / visitors * 100:.2f}% - work out')
print(f'{forbuying / visitors * 100:.2f}% - protein')