

def list_manipulator(the_list,command,second_com,*args):


    if command == 'remove':
        if second_com == 'end':
            if not args:
                the_list.pop(-1)
            else:
                for s in range(*args):
                    the_list.pop(-1)


        elif second_com == 'beginning':
            if not args:
                the_list.pop(0)
            else:
                for s in range(*args):
                    the_list.pop(0)



    elif command == 'add':
        if second_com == 'end':
            for i in range(len(args)):
                the_list.append(args[i])




        elif second_com == 'beginning':
            args = args[::-1]


            for i in range(len(args)):

                the_list.insert(0,args[i])

    return the_list





print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))