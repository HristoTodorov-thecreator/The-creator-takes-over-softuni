g = input()  # projection
row = int(input())
hcolumn = int(input())


total = 0
if g == 'Premiere':  # more expensive one
    total = row * hcolumn * 12.00
    print(f'{total:.2f}')

elif g == 'Normal':  # standart price
    total = row * hcolumn * 7.50
    print(f'{total:.2f}')

elif g == 'Discount':   # discount for students
    total = row * hcolumn * 5.00
    print(f'{total:.2f}')
