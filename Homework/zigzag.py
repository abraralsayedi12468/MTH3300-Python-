#******************************************************************************
# zigzag.py
#******************************************************************************
# Name: Abrar Alsayedi 
#******************************************************************************
# Remarks (optional):
#
#
#
import turtle
import math

#get values for z and p 
z = int(input("Enter int z: "))
p = int(input("Enter int p: "))

#activate the turtle thingy 
screen = turtle.Screen()
zig = turtle.Turtle()
zig.speed(0)

#getting a normal looking zigzag length and gap size 
length = 40
gap = 30

start_x = zig.xcor()
start_y = zig.ycor()

#first for loop the line gets the number of lines, so the rows which comes into affect after every zigzag is drawn 
for line in range(z):
    zig.penup()
    zig.goto(start_x, start_y - line * gap)
    zig.setheading(0)
    zig.pendown()

    #nested loop is like columns but it gives you how many like lines for the zipzag based on z and p 
    for i in range(p):
        zig.right(45)
        zig.forward(length)
        zig.left(90)
        zig.forward(length)
        zig.right(45)

    zig.penup()

    #this part resets the turtle to the same left starting point for each new zigzag line

#ends activity
turtle.done()