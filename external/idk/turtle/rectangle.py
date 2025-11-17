import turtle

t = turtle.Turtle()

t.color("LightCoral")
# t.begin_fill()
# t.right(45)
# t.forward(120)
# t.right(90)
# t.forward(120)
# t.right((180-45))
# t.forward(180)
# t.end_fill()

# t.begin_fill()
# t.forward(100)
# t.right(90)
# t.forward(150)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.end_fill()

# t.begin_fill()
# t.circle(100)
# t.end_fill()

# Move turtle to a point (for example x=50, y=50)
t.penup()
t.goto(50, 50)
t.pendown()

# Draw a circle at that point
t.circle(40)

turtle.done()
