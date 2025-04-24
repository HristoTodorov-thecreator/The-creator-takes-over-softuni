import os


def save(dir_name,first_level=False):

    for filename in os.listdir(dir_name):
        file = os.path.join(dir_name,filename)

        if os.path.isfile(file):
            extension = filename.split('.')[-1]

            if extension not in extensions:
                extensions[extension] = []

            extensions[extension].append(filename)
        elif os.path.isdir(file) and not first_level:
            save(file,first_level=True)



directory = input()

extensions = {}

result = []
try:
    save(directory)
except FileNotFoundError:
    print(f'Dir not found')


extensions = sorted(extensions.items(),key=lambda x: x[0])


for ex ,files in extensions:
    result.append(f'.{ex}')
    for file in sorted(files):
        result.append(f'- - - {file}')

with open('files_/rep.txt', 'w') as report_file:
    report_file.write('\n'.join(result))

