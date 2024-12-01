n = int(input())

p1 , p2 ,p3 ,p4 ,p5 = 0 , 0 , 0 , 0 , 0


for _ in range(n):
    g =int(input())

    if g < 200:
        p1 = p1 + 1
    elif g < 400:
        p2 = p2 + 1
    elif g < 600:
        p3 = p3 + 1
    elif g < 800:
        p4 = p4 + 1
    else:
        p5 = p5 + 1

print(f'{p1 / n * 100:.2f}%')
print(f'{p2 / n * 100:.2f}%')
print(f'{p3 / n * 100:.2f}%')
print(f'{p4 / n * 100:.2f}%')
print(f'{p5 / n * 100:.2f}%')
