#Lab link: https://learn.bcit.ca/d2l/le/content/1008637/viewContent/9805880/View (Fractals with Python turtle)
import turtle
t = turtle.Turtle()

t.forward(100)
t.right(120)
t.forward(100)
t.right(120)
t.forward(100)
t.right(120)

def koch_snowflake(length):
    if length <= 0.1:
        pass
    else:
        pass