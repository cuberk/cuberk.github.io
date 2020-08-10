from turtle import *
from tkinter import *
import turtle
import time

for i in range(3):
  turtle.hideturtle()
  turtle.pencolor('green')
  turtle.pensize(4)
  turtle.penup()
  turtle.setpos(-50, -50)
  turtle.pendown()
  turtle.goto(-50, 50)
  turtle.goto(50, 50)
  turtle.goto(50, -50)
  turtle.goto(-50, -50)
  ts = turtle.getscreen()
  ts.getcanvas().postscript(file="img.eps"+str(i))
  time.sleep(1)
  turtle.reset()

