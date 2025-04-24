number_of_guests = int(input())
normal_guests = set()
vip_guests = set()

guest_at_the_party = set()

numbers = ('0','1','2','3','4','5','6','7','8','9')
for i in range(number_of_guests):
    code = input()
    if code.startswith(numbers):
        vip_guests.add(code)
    else:
        normal_guests.add(code)




while True:
    command = input()
    if command == 'END':
        break
    guest_at_the_party.add(command)

vip_guests = sorted(vip_guests)
normal_guests = sorted(normal_guests)
counter = 0
not_come_v = []
not_come = []

for s in vip_guests:
    if s not in guest_at_the_party:
        counter += 1
        not_come_v.append(s)

for t in normal_guests:
    if t not in guest_at_the_party:
        counter += 1
        not_come.append(t)

print(counter)
for o in not_come_v:
    print(o)

for l in not_come:
    print(l)

