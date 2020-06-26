import time
import turtle
from turtle import Turtle
import random

# Window Setup
win = turtle.Screen()
win.title("Turtle Race")
turtle.bgcolor("navy")
turtle.color("white")
turtle.speed(0)
turtle.penup()
turtle.setpos(-140, 250)
turtle.write("Turtle Race", font=("Arial", 40, "bold"))
turtle.penup()

# Sand
turtle.setpos(-700, -200)
turtle.color("goldenrod")
turtle.begin_fill()
turtle.pendown()
turtle.fd(1600)
turtle.right(90)
turtle.fd(300)
turtle.right(90)
turtle.fd(1600)
turtle.right(90)
turtle.fd(300)
turtle.end_fill()

# Finish Line
stamp_size = 20
square_size = 15
finish_line = 500

turtle.color("white")
turtle.shape("square")
turtle.shapesize(square_size / stamp_size)
turtle.penup()

for i in range(14):
    turtle.setpos(finish_line, (245 - i * square_size * 2))
    turtle.stamp()

for j in range(14):
    turtle.setpos(finish_line + square_size, ((245 - square_size) - (j * square_size * 2)))
    turtle.stamp()

turtle.color("black")
turtle.shape("square")
turtle.shapesize(square_size / stamp_size)
turtle.penup()
for k in range(14):
    turtle.setpos(finish_line + square_size, ((260 - square_size) - (k * square_size * 2)))
    turtle.stamp()

for l in range(14):
    turtle.setpos(finish_line, (230 - l * square_size * 2))
    turtle.stamp()

turtle.hideturtle()

# Turtle 1
turtle_1 = Turtle()
turtle_1.speed(0)
turtle_1.color("red")
turtle_1.shape("turtle")
turtle_1.penup()
turtle_1.goto(-500, 200)
turtle_1.pendown()

# Turtle 2
turtle_2 = Turtle()
turtle_2.speed(0)
turtle_2.color("orange")
turtle_2.shape("turtle")
turtle_2.penup()
turtle_2.goto(-500, 150)
turtle_2.pendown()

# Turtle 3
turtle_3 = Turtle()
turtle_3.speed(0)
turtle_3.color("yellow")
turtle_3.shape("turtle")
turtle_3.penup()
turtle_3.goto(-500, 100)
turtle_3.pendown()

# Turtle 4
turtle_4 = Turtle()
turtle_4.speed(0)
turtle_4.color("green")
turtle_4.shape("turtle")
turtle_4.penup()
turtle_4.goto(-500, 50)
turtle_4.pendown()

# Turtle 5
turtle_5 = Turtle()
turtle_5.speed(0)
turtle_5.color("light blue")
turtle_5.shape("turtle")
turtle_5.penup()
turtle_5.goto(-500, 0)
turtle_5.pendown()

# Turtle 6
turtle_6 = Turtle()
turtle_6.speed(0)
turtle_6.color("indigo")
turtle_6.shape("turtle")
turtle_6.penup()
turtle_6.goto(-500, -50)
turtle_6.pendown()

# Turtle 7
turtle_7 = Turtle()
turtle_7.speed(0)
turtle_7.color("violet")
turtle_7.shape("turtle")
turtle_7.penup()
turtle_7.goto(-500, -100)
turtle_7.pendown()

time.sleep(1) # Pause the game for 1 second before starting the race

# Move the turtles
number_1 = random.randint(5,10)
number_2 = random.randint(5,10)
number_3 = random.randint(5,10)
number_4 = random.randint(5,10)
number_5 = random.randint(5,10)
number_6 = random.randint(5,10)
number_7 = random.randint(5,10)

for i in range(200):
    turtle_1.fd(number_1)
    turtle_2.fd(number_2)
    turtle_3.fd(number_3)
    turtle_4.fd(number_4)
    turtle_5.fd(number_5)
    turtle_6.fd(number_6)
    turtle_7.fd(number_7)   

turtle.exitonclick()

# TO IMPROVE
"""
- Make the game so that when the turtles cross the finish line they stay there
- Display the winning turtle - (on the screen or the source editor)
- Save scores in a text file
"""
