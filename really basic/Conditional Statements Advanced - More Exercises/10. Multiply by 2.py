while True:
    g= float(input())
    if g < 0:
        print(f'Negative number!')
        break
    total = g * 2
    print(f'Result: {total:.2f}')