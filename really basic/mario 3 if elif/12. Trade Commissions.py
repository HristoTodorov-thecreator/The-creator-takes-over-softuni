city_ = input()
sales_ = float(input())

total = 0

if city_ == 'Sofia':
    if 0 <= sales_ <= 500:
        total = sales_ * 0.05
        print(f'{total:.2f}')
    elif 500 <= sales_ <= 1000:
        total = sales_ * 0.07
        print(f'{total:.2f}')
    elif 1000 <= sales_ <= 10000:
        total = sales_ * 0.08
        print(f'{total:.2f}')
    elif sales_ > 10000:
        total = sales_ * 0.12
        print(f'{total:.2f}')
    else:
        print('error')

elif city_ == 'Varna':
    if 0 <= sales_ <= 500:
        total = sales_ * 0.045
        print(f'{total:.2f}')
    elif 500 <= sales_ <= 1000:
        total = sales_ * 0.075
        print(f'{total:.2f}')
    elif 1000 <= sales_ <= 10000:
        total = sales_ * 0.10
        print(f'{total:.2f}')
    elif sales_ > 10000:
        total = sales_ * 0.13
        print(f'{total:.2f}')
    else:
        print('error')

elif city_ == 'Plovdiv':
    if 0 <= sales_ <= 500:
        total = sales_ * 0.055
        print(f'{total:.2f}')
    elif 500 <= sales_ <= 1000:
        total = sales_ * 0.08
        print(f'{total:.2f}')
    elif 1000 <= sales_ <= 10000:
        total = sales_ * 0.12
        print(f'{total:.2f}')
    elif sales_ > 10000:
        total = sales_ * 0.145
        print(f'{total:.2f}')
    else:
        print('error')

else:
    print("error")