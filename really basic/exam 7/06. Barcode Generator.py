first_number = input()
second_number = input()

a , b , c ,d = int(first_number[0]) , int(first_number[1]) , int(first_number[2]) , int(first_number[3])
a1 , b1, c1, d1 = int(second_number[0]) , int(second_number[1]) , int(second_number[2]) , int(second_number[3])

for i in range (a ,a1 + 1):
    for k in range (b , b1 + 1):
        for j in range (c , c1 +1):
            for n in range (d , d1 + 1):
                if i % 2 != 0 and k % 2 != 0 and j % 2 != 0 and n % 2 != 0:
                    print(f'{i}{k}{j}{n}' , end= ' ')