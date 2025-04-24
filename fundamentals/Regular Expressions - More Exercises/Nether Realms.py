g  = input().split(",")
g = [demon.strip() for demon in g]

import re

symbols = ['0','1','2','3','4','5','6','7','8','9','.','+','-','*','/']


demons = {}

for m in g:
    total = 0
    for i in m:
        if i in symbols:
            continue
        else:

            total += ord(i)
    numbers = re.findall(r'[+-]?\d+(?:\.\d+)?', m)
    base_damage = sum(float(num) for num in numbers)
    for char in m:
        if char == '*':
            base_damage *= 2
        elif char == '/':
            base_damage /= 2

    demons[m] = {'health':total,'damage':base_damage}

if demons:
    for p in sorted(demons.keys()):
        print(f"{p} - {demons[p]['health']} health, {demons[p]['damage']:.2f} damage")