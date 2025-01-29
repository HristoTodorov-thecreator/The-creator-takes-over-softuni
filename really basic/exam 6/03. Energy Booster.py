

fruit = input()
size = input()
number_sets = int(input())
price =0
if fruit == 'Watermelon':
    if size == 'small':
        price = 2 * 56

    elif size == 'big':
        price = 5 * 28.70

elif fruit == 'Mango':
    if size == 'small':
        price = 2 * 36.66

    elif size == 'big':
        price = 5 * 19.60

elif fruit == 'Pineapple':
    if size == 'small':
        price = 2 * 42.10

    elif size == 'big':
        price = 5 * 24.80
elif fruit == 'Raspberry':
    if size == 'small':
        price = 2 * 20

    elif size == 'big':
        price = 5 * 15.20

total = price * number_sets

if 400 <= total <= 1000:
    total = total- (total * 0.15)
elif total > 1000 :
    total = total  / 2

print(f"{total:.2f} lv.")

