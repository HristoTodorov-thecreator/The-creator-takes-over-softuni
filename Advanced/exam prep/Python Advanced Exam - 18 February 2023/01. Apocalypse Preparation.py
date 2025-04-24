from collections import deque

textiles = deque([int(x) for x in input().split()])
medicaments = [int(x) for x in input().split()]


data = {30:'Patch',40:'Bandage',100:'MedKit'}

data2 = {'Patch':0,'Bandage':0,'MedKit':0}


while textiles and medicaments:
    textile = textiles.popleft()
    medicament = medicaments.pop()

    result = textile + medicament

    if result in data:
        item = data[result]

        data2[item] += 1
        continue

    elif result > 100:
        data2['MedKit'] += 1
        remaining = result - 100
        if medicaments:
            medicaments[-1] += remaining
        else:
            medicaments.append(remaining)
        continue

    medicament += 10
    medicaments.append(medicament)

if not medicaments and not textiles:
    print(f'Textiles and medicaments are both empty.')
elif not medicaments:
    print(f'Medicaments are empty.')
elif not textiles:
    print(f'Textiles are empty.')

for item, count in sorted(data2.items(), key=lambda x: (-x[1], x[0])):
    if count > 0:
        print(f"{item} - {count}")



if medicaments:
    print(f'Medicaments left: {", ".join(map(str,reversed(medicaments)))}')
if textiles:
    print(f'Textiles left: {", ".join(map(str,textiles))}')



