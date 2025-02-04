

size_egg  ,color_egg, number= input() , input() ,int(input())
price = 0
if size_egg == 'Large':
    if color_egg == 'Red':
        price = 16
    elif color_egg == 'Green':
        price = 12
    elif color_egg == 'Yellow':
        price = 9

elif size_egg == 'Medium':
    if color_egg == 'Red':
        price = 13
    elif color_egg == 'Green':
        price = 9
    elif color_egg == 'Yellow':
        price = 7

elif size_egg == 'Small':
    if color_egg == 'Red':
        price = 9
    elif color_egg == 'Green':
        price = 8
    elif color_egg == 'Yellow':
        price = 5


total = number * price
expense = total * 0.35
total_with_expense = total - expense

print(f'{total_with_expense:.2f} leva.')