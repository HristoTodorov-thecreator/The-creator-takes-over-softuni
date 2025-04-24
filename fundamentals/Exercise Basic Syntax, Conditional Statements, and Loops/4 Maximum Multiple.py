devisor = int(input())
boundary = int(input())

for number in range(boundary,devisor - 1,-1):
    if number % devisor == 0:
        break

print(number)

