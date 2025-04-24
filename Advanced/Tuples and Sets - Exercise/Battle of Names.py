n = int(input())

row = 0

odd = set()
even = set()


for i in range(n):
    total = 0
    name = input()

    for s in name:
        total += int(ord(s))
    row += 1
    total = total // row
    if total % 2 == 0:
        even.add(total)
    else:
        odd.add(total)


odd_sum = sum(odd)
even_sum = sum(even)



if odd_sum == even_sum:
    result = odd.union(even)
elif odd_sum > even_sum:
    result = odd.difference(even)
else:
    result = odd.symmetric_difference(even)

print(', '.join(map(str,result)))
