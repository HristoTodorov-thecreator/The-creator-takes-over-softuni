given_number = int(input())

list_with_numbers = []

filtered = []

for i in range(1,given_number + 1):
    number = int(input())
    list_with_numbers.append(number)

option = input()

if option == 'positive':
    for n in list_with_numbers:
        if n >=0:
            filtered.append(n)
elif option == 'negative':
    for s in list_with_numbers:
        if s < 0:
            filtered.append(s)

elif option == 'even':
    for k in list_with_numbers:
        if k % 2 ==0:
            filtered.append(k)

elif option == 'odd':
    for t in list_with_numbers:
        if t % 2 !=0:
            filtered.append(t)

print(filtered)



