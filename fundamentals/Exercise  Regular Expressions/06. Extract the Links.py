import re

command = input()

pattern = r'(w{3}\.[A-Za-z0-9-]+(\.[a-z]+)+)'

while command:








     x = re.search(pattern,command)
     if x:
          adress = x.group(1)
          print(adress)



     command = input()

