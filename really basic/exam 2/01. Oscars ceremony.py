rent = int(input())


statuettes = rent - (rent * 0.30)
catering = statuettes - (statuettes * 0.15)
sounding = catering / 2

total = statuettes + catering + sounding + rent
print(f'{total:.2f}')