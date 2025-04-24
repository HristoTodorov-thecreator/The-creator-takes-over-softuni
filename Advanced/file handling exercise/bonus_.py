import os
import re

directory = input()

string_one = input()
second_string = input()

for filename in os.listdir(directory):
    file = os.path.join(directory,filename)

    if os.path.isfile(file):
        newname = filename.replace(string_one,second_string)
        new_file = '/'.join(re.split(r'[\\/]',file)[:-1]) +'/' + newname
        os.rename(file,new_file)