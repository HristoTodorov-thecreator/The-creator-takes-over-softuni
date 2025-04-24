first = input()
second = input()

def char():

   list = []
   for i in range(ord(first) + 1,ord(second)):
       list.append(chr(i))
   return list

the_list = char()
print(' '.join(the_list))