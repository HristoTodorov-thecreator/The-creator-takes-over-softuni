my_dict  = {}  # prazen re4nik
print(my_dict)  # dict polzvat klu4 za dostup do stoinostite

my_dict = {   # dict
    'name' : 'ivan',
    'city' : 'sofia',
    'age' : 25
}

print(my_dict['city'])  # printirane na dict
print(my_dict['age'])

my_dict['age'] = 27  # promqna na dict ili dobavqne

print(my_dict['age'])
my_dict['work'] = 'programist'
print(my_dict)


del my_dict['age']  # iztrivane na elementi

for key in my_dict:  # minava prez dicta
    print(key)

for value in my_dict.values():
    print(value)

for key,value in my_dict.items():
    print(key , value)