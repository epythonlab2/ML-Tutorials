import turtle
import colorsys

# setup
t = turtle.Turtle()
t.speed(0)
turtle.bgcolor('black')

# Color palette
hue = 0
n = 100
# Draw spiral
for i in range(360):
    col = colorsys.hsv_to_rgb(
        hue, 1, 1
    )
    t.pencolor(col)
    t.forward(i * 2)
    t.right(59)
    hue += 1/n 
    if hue > 1:
        hue = 0
turtle.done()
    
