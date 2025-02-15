g = int(input())
counter =0
n = g + 1
for i in range (1,g + 1):
    counter += 1
    if counter == 1:

        print(' ' * n +'|')





    print(f"{' ' * (g - i) }{'*' * i} { '|'} {'*' * i}")