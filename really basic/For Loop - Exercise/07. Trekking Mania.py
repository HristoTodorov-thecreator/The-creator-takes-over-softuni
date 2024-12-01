number_of_groups = int(input())

p1 ,p2,p3,p4,p5 = 0 ,0 ,0 ,0 ,0

for _ in range (number_of_groups):
    groups = int(input())
    if groups <= 5:
        p1 =p1+ groups
    elif 6 <= groups <= 12:
        p2 =p2 + groups
    elif 13 <= groups <= 25:
        p3 =p3 + groups
    elif 26 <= groups <= 40:
        p4 = p4 +groups
    elif groups >= 41:
        p5 =p5 + groups

totalpeople = p1 + p2 +p3 + p4 + p5


print(f'{p1 /totalpeople * 100:.2f}%')
print(f'{p2 /totalpeople * 100:.2f}%')
print(f'{p3 /totalpeople * 100:.2f}%')
print(f'{p4 /totalpeople * 100:.2f}%')
print(f'{p5 /totalpeople * 100:.2f}%')


