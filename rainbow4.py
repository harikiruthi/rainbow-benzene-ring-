
# Python program to draw
# Rainbow Benzene
# using Turtle Programming
import turtle
import playsound
from playsound import playsound
playsound('Ending-sound-effect.mp3')
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow','pink','white','brown']
t = turtle.Pen()
turtle.bgcolor('black')
for x in range(180):
    t.pencolor(colors[x%9])
    t.width(x/100 + 1)
    t.forward(x)
    t.left(59)