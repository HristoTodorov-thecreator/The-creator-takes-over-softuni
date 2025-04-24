import time

numbers = list(map(int,input().split()))
target = int(input())

targets = set()

values_map = {}
start = time.time()
for value in numbers:
    if value in targets:
        targets.remove(value)
        pair = values_map[value]
        del values_map[value]
        print(f'{pair} + {value} = {target}')

    else:
        resulting_number = target - value
        targets.add(resulting_number)
        values_map[resulting_number]= value

end = time.time()
print(f'Time range: {end-start}')