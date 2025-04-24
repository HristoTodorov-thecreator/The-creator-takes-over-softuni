list_with_numbers = list(map(int,input().split()))

middle_index = len(list_with_numbers) // 2

left_car = list_with_numbers[:middle_index]
right_car = list_with_numbers[middle_index + 1:]

def calculate(car):
    total_time = 0

    for time in car:
        total_time += time
        if time == 0:
            total_time -= (total_time * 0.20)
    return  total_time

left_time = calculate(left_car)
right_time = calculate(right_car[::-1])

if left_time < right_time:
    winner = "left"
    total_time = left_time
else:
    winner = "right"
    total_time = right_time

print(f"The winner is {winner} with total time: {total_time:.1f}")
