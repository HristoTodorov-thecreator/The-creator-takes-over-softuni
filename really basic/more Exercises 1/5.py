
w = float(input()) * 100
h = float(input()) * 100

door_with_department = 3
corridor = 100

totalw = w // 120
totalh = (h - corridor) // 70
n = totalw * totalh - door_with_department

print(n)