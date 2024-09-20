hour_test = int(input())
minutes_test = int(input())
hour_arrive = int(input())
minutes_arrive = int(input())

test_total = (hour_test * 60) + minutes_test  # minutes test
arrive_total = (hour_arrive * 60) + minutes_arrive  # minutes arrive

total_difference = test_total - arrive_total

if  0 <= total_difference <= 30:
    print("On time")
elif total_difference < 0:
    print("Late")
elif total_difference > 30:
    print("Early")

hours = abs(total_difference) // 60
minutes = abs(total_difference) % 60

result = ""

if hours > 0:
    result = f'{hours}:{minutes:02d} hours'
elif minutes > 0:
    result = f'{minutes} minutes'

if total_difference > 0:
    result += ' before the start'
elif total_difference < 0:
    result += ' after the start'

print(result)