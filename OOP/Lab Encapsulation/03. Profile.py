

class Profile:

    def __init__(self,username,password):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username
    
    @username.setter
    def username(self, value):
        if len(value) < 5 or len(value) > 15:
            raise ValueError('The username must be between 5 and 15 characters.')
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if len(value) < 8:
            raise ValueError('The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.')
        check_one = len([c for c in value if c.isdigit()])

        if not check_one:
            raise ValueError('The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.')

        check_two = len([c for c in value if c.isupper()])
        if not check_two:
            raise ValueError('The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.')

        self.__password = value

    def __str__(self):
        return f'You have a profile with username: "{self.__username}" and password: {"*" * len(self.__password)}'
