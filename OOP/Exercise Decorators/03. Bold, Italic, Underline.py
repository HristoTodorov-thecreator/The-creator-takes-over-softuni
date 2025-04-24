
def make_bold(n):
    def wrapper(*args):
        return f'<b>{n(*args)}</b>'


    return wrapper

def make_italic(n):
    def wrapper(*args):
        return f'<i>{n(*args)}</i>'


    return wrapper


def make_underline(n):
    def wrapper(*args):
        return f'<u>{n(*args)}</u>'


    return wrapper




@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"
print(greet("Peter"))
