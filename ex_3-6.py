Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> import turtle
>>> t = turtle.Turtle()
>>> t.shape("turtle")
>>> 
>>> x1 = int(input("x1= "))
x1= 0
>>> y1 = int(input("y1= "))
y1= 0
>>> x2 = int(input("x2= "))
x2= 100
>>> y2 = int(input("y2= "))
y2= 100
>>> 
>>> t.goto(x1,y1)
>>> t.goto(x2,y2)
>>> dist = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
>>> 
>>> t.up()
>>> t.write("점의 길이= ", dist)
>>> t.write(dist)
>>> t.goto(x2,y2)
