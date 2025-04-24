import turtle

turtle.bgcolor('black')
t= turtle.Turtle()

colors = ['red','dark red']
t.speed(0)
for i in range(400):
    t.forward(i+1)
    t.right(89)
    t.pencolor(colors[i%2])

turtle.done()