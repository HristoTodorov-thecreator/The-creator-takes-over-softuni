combination = 0

# x1 + x2 + x3 = n
nmagic = int(input())
for x1 in range (0 ,nmagic + 1):
    for x2 in range(0 ,nmagic + 1):
        for x3 in range (0 ,nmagic + 1):
            if x1 + x2 + x3 == nmagic:
                combination += 1

print(combination)

