
junior = int(input())
senior = int(input())
totalpeople = junior + senior
type_track = input()
totalj = 0
totals = 0

if type_track == 'trail':
    totalj = junior * 5.50
    totals = senior * 7
elif type_track == 'cross-country':
    totalj = junior * 8
    totals = senior * 9.50
elif type_track == 'downhill':
    totalj = junior * 12.25
    totals = senior * 13.75
elif type_track == 'road':
    totalj = junior * 20
    totals = senior * 21.50

totalsum = totalj + totals
if totalpeople >= 50 and type_track == 'cross-country':
    totalsum = totalsum - (totalsum * 0.25)

expenses = totalsum * 0.05
total_with_expenses = totalsum - expenses

print(f'{total_with_expenses:.2f}')
