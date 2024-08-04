counter = 0
thesum = int(input())
incard = 0
withpaper = 0
counter_for_people = 0
coun_p_2 = 0
while True:
    g = input()
    if g == 'End':
        print(f"Failed to collect required money for charity.")
        exit()
    m = int(g)
    counter += 1
    if counter % 2 != 0:
        if m > 100:
            print(f'Error in transaction!')
        else:
            thesum -= m
            print(f'Product sold!')
            withpaper += m
            counter_for_people += 1


    else:
        if m < 10:
            print(f'Error in transaction!')
        else:
            thesum -= m
            print(f'Product sold!')
            incard += m
            coun_p_2 += 1

    if thesum <= 0:
        break

print(f"Average CS: {withpaper / counter_for_people:.2f}")
print(f"Average CC: {incard / coun_p_2:.2f}" )

