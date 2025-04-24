type_ = input()
data_ = input()




def stringo(data_):
    return f'${data_}$'

def into(data_):
    return int(data_) * 2

def realo(data_):
    return f'{float(data_) * 1.5:.2f}'

if type_ == 'int':
    print(into(data_))

elif type_ == 'real':
    print(realo(data_))

elif type_ == 'string':
    print(stringo(data_))