num_mans = int(input())
num_womans = int(input())
num_max_tables = int(input())


counter = 0
for i in range (1,num_mans + 1):
    for z in range(1,num_womans + 1):

        if counter < num_max_tables:



            print(f'({i} <-> {z}) ',end='')
            counter += 1
        else:
            break
