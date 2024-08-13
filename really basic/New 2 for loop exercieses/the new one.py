
g = int(input())

oddsum = 0
oddmin = float('inf')
oddmax = float('-inf')
evensum = 0
evenmin = float('inf')
evenmax = float('-inf')


counter1 = 0
counter2 = 0


for i in range(1 ,g + 1):
    number = float(input())
    if g == 0:
        break


    if i % 2 == 0:
        evensum += number
        if number < evenmin:
            evenmin = number
        if number > evenmax:
            evenmax = number
    else:
        oddsum += number
        if number < oddmin:
            oddmin = number
        if number > oddmax:
            oddmax = number

if oddsum != 0:
    print(f"OddSum={oddsum:.2f},")
    print(f"OddMin={oddmin:.2f},")
    print(f"OddMax={oddmax:.2f},")
else:
    print(f"OddSum={oddsum:.2f},")
    print("OddMin=No,")
    print("OddMax=No,")


if evensum != 0:
    print(f"EvenSum={evensum:.2f},")
    print(f"EvenMin={evenmin:.2f},")
    print(f"EvenMax={evenmax:.2f}")
else:
    print(f"EvenSum={evensum:.2f},")
    print("EvenMin=No,")
    print("EvenMax=No")
