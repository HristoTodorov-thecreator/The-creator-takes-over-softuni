from collections import deque
programmer_times = deque([int(x) for x in input().split()])

number_of_tasks = [int(x) for x in input().split()]

Darth_Vader_Duckys = 0
Thor_Duckys = 0
Big_Blue_Rubber_Duckys = 0
Small_Yellow_Rubber_Duckys = 0

while programmer_times and number_of_tasks:
    programmer = programmer_times.popleft()
    value_task = number_of_tasks.pop()

    total = programmer * value_task

    if 0 <= total <= 60:
        Darth_Vader_Duckys += 1
    elif 61 <= total <= 120:
        Thor_Duckys += 1
    elif 121 <= total <= 180:
        Big_Blue_Rubber_Duckys += 1
    elif 181 <= total <= 240:
        Small_Yellow_Rubber_Duckys += 1
    elif total > 240:
        value_task -= 2
        programmer_times.append(programmer)
        number_of_tasks.append(value_task)


print(f"Congratulations, all tasks have been completed! Rubber ducks rewarded:")

print(f'Darth Vader Ducky: {Darth_Vader_Duckys}')
print(f'Thor Ducky: {Thor_Duckys}')
print(f'Big Blue Rubber Ducky: {Big_Blue_Rubber_Duckys}')
print(f'Small Yellow Rubber Ducky: {Small_Yellow_Rubber_Duckys}')



