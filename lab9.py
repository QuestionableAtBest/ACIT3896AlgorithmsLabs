#Lab link: https://learn.bcit.ca/d2l/le/content/1008637/viewContent/9805880/View (Fractals with Python turtle)
import turtle
t = turtle.Turtle()

#Moving him back a bit because the snowflake gets cut off
t.penup()
t.backward(200)
t.pendown()

def draw_koch_line(length, depth):
    if depth == 0:
        t.forward(length)
    else:
        draw_koch_line(length/3, depth-1)
        t.left(60)
        draw_koch_line(length/3, depth-1)
        t.right(120)
        draw_koch_line(length/3, depth-1)
        t.left(60)
        draw_koch_line(length/3, depth-1)

t.speed(10)
for i in range(3):
    draw_koch_line(500, 4)
    t.right(120)