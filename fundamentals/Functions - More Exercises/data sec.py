def process_data(data, type_):
    if type_ == 'int':
        return int(data) * 2
    elif type_ == 'string':
        return f'${data}$'
    elif type_ == 'real':
        return f'{float(data) * 1.5:.2f}'


type_ = input()
data_ = input()


print(process_data(data_, type_))