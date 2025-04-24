import turtle

t = turtle.Turtle()
turtle.bgcolor('black')
colors = ['yellow','orange']
t.speed(0)
for s in range(200):
    t.forward(s+10)
    t.right(89)
    t.color(colors[s%2])

turtle.done()