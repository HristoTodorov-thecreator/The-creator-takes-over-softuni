start = int(input())
end = int(input())
magic = int(input())
flag = False

combination = 0
for i in range(start , end+1):
    for k in range (start, end +1):

         combination += 1
         if i + k == magic:
             print(f'Combination N:{combination} ({i} + {k} = {magic})')
             flag = True
             break
    if flag:
        break

else:
    print(f"{combination} combinations - neither equals {magic}")