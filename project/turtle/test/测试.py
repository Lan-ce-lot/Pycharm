
import turtle
 
turtle.pensize(3)
turtle.penup()
turtle.goto(-100, -50)
turtle.pendown()
turtle.begin_fill()
turtle.color("red")
turtle.circle(40, steps=3)
turtle.end_fill()
 
turtle.penup()
turtle.goto(0, -50)
turtle.pendown()
turtle.begin_fill()
turtle.color("yellow")
turtle.circle(50)
turtle.end_fill()
 
turtle.penup()
turtle.goto(100, -50)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("green")
turtle.circle(40, steps=6)
turtle.end_fill()
 
turtle.penup()
turtle.goto(-50, 100)
turtle.pendown()
turtle.color("blue")
turtle.write("Colorful Shapes",  font = ("Times", 18,"bold"))
turtle.end_fill()
 
turtle.hideturtle()
 
turtle.done()

