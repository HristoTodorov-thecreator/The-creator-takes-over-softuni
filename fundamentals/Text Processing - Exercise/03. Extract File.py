g = input().split("\\")
splited = g[-1]

splitthis = splited.split('.')

print(f'File name: {splitthis[0]}')

print(f'File extension: {splitthis[-1]}')