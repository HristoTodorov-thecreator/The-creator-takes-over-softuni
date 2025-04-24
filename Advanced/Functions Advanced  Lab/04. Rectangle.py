

def rectangle(length,width):
    if not isinstance(length,int) or not isinstance(width,int):
        return  f"Enter valid values!"

    def area():
        return width * length


    def perimeter():
        return width*2 + length*2

    return f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"


print(rectangle(2, 10))

