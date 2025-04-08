players = input().split(', ')

data_ = {}

while True:
    info_ = input()
    if info_ == 'end of race':
        break
    the_sum = 0
    the_name = ''

    for i in info_:
        if i.isdigit():
            the_sum += int(i)
        if i.isalpha():
            the_name += i
    if the_name in players:
        if the_name not in data_:
            data_[the_name] = 0
            data_[the_name] += the_sum
        else:
            data_[the_name] += the_sum


sorted_data = sorted(data_.items(), key=lambda x: x[1], reverse=True)

counter = 1
for o,p in sorted_data:
    if counter == 1:
        print(f'{counter}st place: {o}')
    elif counter == 2:
        print(f'{counter}nd place: {o}')

    if counter == 3:
        print(f'{counter}rd place: {o}')
        break

    counter += 1
