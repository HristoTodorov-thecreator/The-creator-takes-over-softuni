n = int(input("Enter the size of the square: "))

# Печат на първия ред
print('*' * n)

# Печат на средните редове
for _ in range(n - 2):
    print('*' + ' ' * (n - 2) + '*')

# Печат на последния ред
print('*' * n)