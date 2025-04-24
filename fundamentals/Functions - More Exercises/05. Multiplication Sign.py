a = int(input())
b = int(input())
c = int(input())

if a == 0 or b == 0 or c == 0:
    print(f'zero')



else:
    neg_count = 0
    if a < 0:
        neg_count += 1

    if b < 0:
        neg_count += 1

    if c < 0:
        neg_count += 1

    if neg_count % 2 ==0:
        print(f'positive')

    else:
        print(f'negative')




