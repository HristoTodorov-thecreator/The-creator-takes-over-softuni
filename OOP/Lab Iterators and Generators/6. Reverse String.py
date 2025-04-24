
def reverse_text(string):

    g = len(string)
    while g > 0:
        g -= 1
        yield string[g]


for char in reverse_text("step"):
    print(char, end='')
