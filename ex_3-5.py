Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> import math
>>> x1 = int(input("x1= "))
x1= 0
>>> y1 = int(input("y1= "))
y1= 0
>>> x2 = int(input("x2= "))
x2= 100
>>> y2 = int(input("y2= "))
y2= 100
>>> dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
>>> print("두점 사이의 거리=", dist)
두점 사이의 거리= 141.4213562373095
>>> import turtle
>>> t = turtle.Turtle()
>>> t.shape("turtle")
>>> t.left(45)
>>> t.forward(141)
>>> t.setheading(0)
>>> t.goto(0,0)
>>> t.forward(100)
>>> t.left(90)
>>> t.forward(100)
>>> t._screen.exitonclick()
