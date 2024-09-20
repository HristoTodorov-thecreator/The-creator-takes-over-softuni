fruit_ = input()
day_ = input()
quantity = float(input())

total = 0

if day_ == 'Monday' or day_ == "Tuesday" or day_ == 'Wednesday' or day_ == "Thursday" or day_ == "Friday":
    if fruit_ == 'banana':
        total = 2.50 * quantity
        print(f'{total:.2f}')
    elif fruit_ == 'apple':
        total = 1.20 * quantity
        print(f'{total:.2f}')
    elif fruit_ == 'orange':
        total = 0.85 * quantity
        print(f'{total:.2f}')
    elif fruit_ == 'grapefruit':
        total = 1.45 * quantity
        print(f'{total:.2f}')
    elif fruit_ == 'kiwi':
        total = 2.70 * quantity
        print(f'{total:.2f}')
    elif fruit_ == 'pineapple':
        total = 5.50 * quantity
        print(f'{total:.2f}')
    elif fruit_ == 'grapes':
        total = 3.85 * quantity
        print(f'{total:.2f}')
    else:
        print('error')

elif day_ == 'Saturday' or day_ == 'Sunday':
    if fruit_ == 'banana':
        total = 2.70 * quantity
        print(f'{total:.2f}')
    elif fruit_ == 'apple':
        total = 1.25 * quantity
        print(f'{total:.2f}')
    elif fruit_ == 'orange':
        total = 0.90 * quantity
        print(f'{total:.2f}')
    elif fruit_ == 'grapefruit':
        total = 1.60 * quantity
        print(f'{total:.2f}')
    elif fruit_ == 'kiwi':
        total = 3.00 * quantity
        print(f'{total:.2f}')
    elif fruit_ == 'pineapple':
        total = 5.60 * quantity
        print(f'{total:.2f}')
    elif fruit_ == 'grapes':
        total = 4.20 * quantity
        print(f'{total:.2f}')
    else:
        print('error')
else:
    print('error')

