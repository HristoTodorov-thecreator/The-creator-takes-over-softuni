n = int(input())
counter = 0
for i in range(n):
    something = input()
    if '(' in something:
        counter += 1
    if ')' in something:
        counter -=1
    if 0 != counter != 1:
        print("UNBALANCED")
        break

else:
    print("BALANCED")
