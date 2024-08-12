country = input()
instrument = input()
max_points = 20

total = 0

if country == 'Russia':
    if instrument == 'ribbon':
        total = 9.100 + 9.400
    elif instrument == 'hoop':
        total = 9.300 + 9.800
    elif instrument == 'rope':
        total = 9.600 + 9.000
elif country == 'Bulgaria':
    if instrument == 'ribbon':
        total = 9.600 + 9.400
    elif instrument == 'hoop':
        total = 9.550 + 9.750
    elif instrument == 'rope':
        total = 9.500 + 9.400
elif country == 'Italy':
    if instrument == 'ribbon':
        total = 9.200 + 9.500
    elif instrument == 'hoop':
        total = 9.450 + 9.350
    elif instrument == 'rope':
        total = 9.700 + 9.150


totalrest = max_points - total
percent = (totalrest /20) * 100


print(f"The team of {country} get {total:.3f} on {instrument}.")
print(f"{percent:.2f}%")