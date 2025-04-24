import re


class NameTooShortError(Exception):
    pass

class MustContainAtSymbolError(Exception):
    pass

class InvalidDomainError(Exception):
    pass

class Morethanoneatsymbol(Exception):
    pass

class InvalidNameError(Exception):
    pass


pattern = r'^[\w.]+$'

VALID = ('com', 'bg', 'net', 'org')



MIN_CHAR = 4
emails = input()


while emails != 'End':
    if emails.count('@') > 1:
        raise Morethanoneatsymbol('Email should countain only one @ symbol')
    elif '@' not in emails:
        raise MustContainAtSymbolError('Email must contain @')
    elif len(emails.split('@')[0]) <= MIN_CHAR:
        raise NameTooShortError('Name must be more than 4 characters')
    elif emails.split('.')[-1] not in VALID:
        raise InvalidDomainError('Domain must be one of the following: .com, .bg, .org, .net')
    elif not re.match(pattern, emails.split('@')[0]):
        raise InvalidNameError("Username contains invalid characters")


    print(f'Email is valid')








    emails = input()

