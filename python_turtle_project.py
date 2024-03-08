import turtle
import colorsys

turtle.bgcolor('black')
turtle.speed('fast')
a = 0.0
turtle.hideturtle()

for i in range (450):
    colors = colorsys.hsv_to_rgb(a,1,1)
    turtle.color(colors)
    a += 0.005

    turtle.forward(i)
    turtle.backward(i)
    turtle.right(180)
    turtle.left(10)
    turtle.tracer(10)

turtle.mainloop()
