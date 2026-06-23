import turtle as t # this allows you to use all turtle methods through t.methodname

t.pensize(8) # set the thickness of the pen

t.penup() # lift the turtle pen so that you're not drawing while moving
t.setx(-300) # move the turtle to a specific horizontal coordinate (remember that 0 is the middle of the screen)
t.sety(400) # move the turtle to a specific vertical coordinate (remember that 0 is the middle of the screen)
t.setpos(-300,400) # move the turtle to a specific coordinate (remember that 0,0 is the middle of the screen)
t.pendown() # return the turtles pen to paper before drawing

t.teleport(-300,400) # move directly to the specific coordinate without drawing on the way

t.color("blue") # changes the colour of pen used

t.forward(600) # move forward 600 places
t.right(90) # turn 90 degrees

t.forward(600)
t.right(90)

t.forward(600)
t.right(90)

t.forward(600)
t.right(90)


t.mainloop() # python won't immediately close the drawing screen