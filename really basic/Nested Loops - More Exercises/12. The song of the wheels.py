
M = int(input())

count = 0
fourth_comb = None

for a in range(1,10):
    for b in range(a + 1 ,10):
        for c in range (1 , 10):
            for d in range ( 1 , c):
                if a * b + c * d == M:
                   count += 1
                   combination = f"{a}{b}{c}{d}"
                   print(f'{combination}' ,end= ' ')
                   if count == 4:
                       fourth_comb = combination

print()

if fourth_comb:
    print(f"Password: {fourth_comb}")
else:
    print("No!")