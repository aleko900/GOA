from turtle import *



width(10)

color("red")
begin_fill()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of square

#driwing a door
begin_fill()
forward(70)
color("black")
left(90)

forward(120)
right(90)

forward(60)
right(90)
forward(120)
end_fill()
#end a door

penup()
goto(200, 200)
pendown()

color("blue")
begin_fill()
right(150)
forward(200)

left(120)
forward(200)
end_fill()

#next

penup()
goto(200, 200)
pendown()
begin_fill()
color("yellow")
left(120)
forward(170)
right(90)
forward(200)
right(90)
forward(170)
end_fill()

#glass
color("cyan")
penup()
goto(250, 150)
pendown()
begin_fill()
left(90)
forward(80)

left(90)
forward(80)

left(90)
forward(80)

left(90)
forward(80)
end_fill()

penup()
goto(200, 200)
pendown()
color("brown")
begin_fill()
left(180)
forward(170)

left(147)
forward(315)
end_fill()
#begin_fill()
#color("blue")
#penup()
#goto(370, 200)
#pendown()
#right(33)
#forward(320)
#end_fill()





exitonclick()