

number_joinery = int(input())
type = input()
delivery = input()


if number_joinery < 10:
    print(f'Invalid order')
    exit()


total = 0
if type == '90X130':
    total = number_joinery * 110
    if number_joinery > 60:
        total = total - (total * 0.08)
    elif number_joinery > 30:
        total = total - (total * 0.05)

elif type == '100X150':
    total = number_joinery * 140
    if number_joinery > 80:
        total = total - (total * 0.10)
    elif number_joinery > 40:
        total = total - (total * 0.06)
elif type == '130X180':
    total = number_joinery * 190
    if number_joinery > 50:
        total = total - (total * 0.12)
    elif number_joinery > 20:
        total = total - (total * 0.07)
elif type == '200X300':
    total = number_joinery * 250
    if number_joinery > 50:
        total = total - (total * 0.14)
    elif number_joinery > 25:
        total = total - (total * 0.09)

if delivery == 'With delivery':
    total += 60

if number_joinery > 99:
    total = total - (total * 0.04)

print(f"{total:.2f} BGN")


