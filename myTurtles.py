import turtle
import random
turtle.bgcolor("black")
width = 1400
height = 700
wn = turtle.Screen()
wn.setup(width, height)

t = turtle.Turtle()
t.speed(10)
t.pencolor("red")
t.width(5)
t.shape("turtle")

o = turtle.Turtle()
o.speed(10)
o.pencolor("blue")
o.width(5)
o.shape("turtle")
o.rt(180)
o.goto(-123,0)


m = turtle.Turtle()
m.speed(10)
m.pencolor("green")
m.width(5)
m.shape("turtle")
m.penup()
m.goto(-360,-300)
m.pendown()
m.rt(270)


colors = ("blue", "purple", "red", "white", "green", "yellow", "OrangeRed", "DarkOrange", "Lime", "DarkViolet",
"MediumVioletRed", "CornflowerBlue", "Aquamarine", "Gold", "Crimson", "Magenta", "Indigo")


for j in range(999) :
    t.forward(100)
    o.forward(100)
    m.pencolor(random.choice(colors))
    m.fd(150)
    t.circle(60)
    m.pencolor(random.choice(colors))
    m.fd(150)
    o.circle(60)
    m.pencolor(random.choice(colors))
    m.fd(150)
    t.pencolor(random.choice(colors))
    t.rt(90)
    m.pencolor(random.choice(colors))
    m.fd(150)
    o.rt(90)
    o.pencolor(random.choice(colors))
    m.rt(90)
    
    
    

   

wn.mainloop()
   

