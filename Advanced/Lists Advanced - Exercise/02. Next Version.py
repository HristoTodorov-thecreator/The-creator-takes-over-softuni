version = input().split('.')

make_into_one = ''


for number in version:
    make_into_one += ''.join(number)

into_one_int = int(make_into_one)

add = into_one_int + 1


new_version = '.'.join(str(add))

print(new_version)








