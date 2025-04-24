password = input()

firstflag = False
secondflag = False
thirdflag = False

counter = 0

def digit():
    numbert = 0
    global firstflag
    for number in password:
        if number.isdigit():
            numbert += 1

    if numbert <2:
        g = f'Password must have at least 2 digits'
        firstflag = True
        return g




def letters():
    global secondflag
    if not 6 <= len(password) <=10:
        secondflag = True
        return f'Password must be between 6 and 10 characters'


def number_and_letters():
    global thirdflag
    if not password.isalnum():
        thirdflag = True
        return f'Password must consist only of letters and digits'

digit()
letters()
number_and_letters()
if secondflag:
    print(letters())
    counter += 1

if thirdflag:
    print(number_and_letters())
    counter += 1

if firstflag:
    print(digit())
    counter += 1



if counter == 0:
    print(f'Password is valid')
