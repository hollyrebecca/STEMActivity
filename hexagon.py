import turtle as t # this allows you to use all turtle methods through t.methodname

t.pensize(8) # set the thickness of the pen

t.teleport(-300,400) # move directly to the specific coordinate without drawing on the way

t.fillcolor("blue") 
t.begin_fill() # any completed shape will be filled in

t.forward(500)
t.right(60) # the angle of a shape is equal to 360 / number of sides

t.forward(500)
t.right(60)

t.forward(500)
t.right(60)

t.forward(500)
t.right(60)

t.forward(500)
t.right(60)

t.forward(500)
t.right(60)

t.end_fill() # fill the completed shape with color

t.done()