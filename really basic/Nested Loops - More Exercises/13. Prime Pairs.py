start1 = int(input())
start2 = int(input())
diff1 = int(input())
diff2 = int(input())

end1 = start1 + diff1
end2 = start2 + diff2

for i in range (start1 , end1 + 1):
    if i < 2:
        continue


    is_prime = True
    for num in range (2 , int(i**0.5) +1):
        if i % num == 0:

           is_prime = False
           break

    if not is_prime:
        continue

    for i2 in range(start2, end2 + 1):
        if i2 < 2:
            continue

        is_prime2 = True
        for num1 in range(2, int(i2 ** 0.5) + 1):
            if i2 % num1 ==0 :

               is_prime2 = False
               break


        if is_prime2:
            print(f'{i}{i2}')