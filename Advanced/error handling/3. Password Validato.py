
class PasswordTooShortError(Exception):
    pass

class PasswordTooCommonError(Exception):
    pass

class PasswordNoSpecialCharactersError(Exception):
    pass


SPECIAL_CHARS = ("@", "*", "&", "%")

class PasswordContainsSpacesError(Exception):
    pass


passwords = input()
MINIMUM_PASSWORD_LEN = 8

def check(pass_,special):
    only_digits = pass_.isdigit()
    only_letters = pass_.isalpha()
    only_special = all(v in special for v in pass_)
    return only_special or only_digits or only_letters

def special_check(pass_,special):
    for i in pass_:
        if i in special:
            return False
    return True


while passwords != 'Done':

    if len(passwords) < MINIMUM_PASSWORD_LEN:
        raise PasswordTooShortError('Password must contain at least 8 characters')


    if check(passwords,SPECIAL_CHARS):
        raise PasswordTooCommonError("Password must be a combination of digits, letters, and special characters")

    if special_check(passwords,SPECIAL_CHARS):
        raise PasswordNoSpecialCharactersError("Password must contain at least 1 special character")




    if " " in passwords:
        raise PasswordContainsSpacesError("Password must not contain empty spaces")



    print("Password is valid")
    password = input()


