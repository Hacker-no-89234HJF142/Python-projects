from sketchpy import library as lib
import turtle
t = turtle.Turtle()
def pos(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
pos(270,-370)
t.pencolor("orange")
t.write("Happy", font=("Arial", 40, "bold"))
pos(140,-200)
t.pencolor("navy")
t.write("75th Independence", font=("Arial", 40, "bold"))
pos(290,-270)
t.pencolor("Green")
t.write("Day", font=("Arial", 40, "bold"))
l = lib.flag()
l.draw()
turtle.done()