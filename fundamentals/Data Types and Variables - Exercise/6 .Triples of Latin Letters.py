given_number = int(input())

for i in range(0,given_number):
    for s in range(0,given_number ):
        for m in range(0,given_number):

            print(f'{chr(97+i)}{chr(97 + s)}{ chr(97 + m)}')