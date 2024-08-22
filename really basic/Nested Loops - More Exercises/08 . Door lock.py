upperfor_hundreds = int(input())
upperfor_tens = int(input())
upperfor_ones = int(input())

for i in range(1,upperfor_hundreds + 1):
    for m in range (1,upperfor_tens + 1):
        for n in range (1,upperfor_ones + 1):
            if i % 2 == 0 and n % 2 == 0:
                if m == 2 or m == 3 or m == 5 or m == 7:
                    print(f'{i} {m} {n}')


