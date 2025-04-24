import turtle

g = turtle.Turtle()
g.color('red','green')
g.speed(1)

g.begin_fill()
for i in range(4):

    g.left(90)
    g.forward(100)

g.end_fill()
turtle.done()
