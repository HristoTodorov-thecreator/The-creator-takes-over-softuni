number = int(input())

even = 0
odd = 0

for i in range (1,number + 1):
    g = int(input())
    if i % 2 == 0:
        even += g
    else:
        odd += g

if odd == even:
    print(f'Yes\nSum = {even}')
else:
    print(f'No\nDiff = {abs(odd - even)}')






