none = int(input())
ntwo = int(input())
operator = input()

total = None

if operator == '+':
    total = f'{none} {operator} {ntwo} = {none + ntwo}' + (' - even' if (none + ntwo) % 2 == 0 else ' - odd')
elif operator == '-':
    total = f'{none} {operator} {ntwo} = {none - ntwo}' + (' - even' if (none - ntwo) % 2 == 0 else ' - odd')
elif operator == '*':
    total = f'{none} {operator} {ntwo} = {none * ntwo}' + (' - even' if (none * ntwo) % 2 == 0 else ' - odd')
elif ntwo == 0:
    total = f"Cannot divide {none} by zero"
elif operator == '/':
    total = f'{none} {operator} {ntwo} = {none / ntwo:.2f}'
elif operator == '%':
    total = f'{none} {operator} {ntwo} = {none % ntwo}'

print(total)