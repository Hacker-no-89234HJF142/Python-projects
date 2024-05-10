

import turtle
import time
screen=turtle.Screen()
trtl=turtle.Turtle()
screen.setup(600,600)
screen.bgcolor("black")
clr=["red","white","blue","yellow","purple","blue","yellow","red","blue","white","yellow","orange","red","white","blue"]
trtl.pensize(8)
trtl.penup()
turtle.setpos(-90,30)
trtl.pendown()
trtl.speed(3)
for i in range(15):
    trtl.pencolor(clr[i])
    trtl.forward(200)
    trtl.right(144)
trtl.penup()    
trtl.septos(80,-140)    
trtl.pendown()    
trtl.pencolor("olive")    
trtl.write("Subscribe To My Channel",font=("Arial",12,"normal"))  
trtl.ht()