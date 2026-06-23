import turtle as t # this allows you to use all turtle methods through t.methodname

t.pensize(8) # set the thickness of the pen

t.teleport(-300,400) # move directly to the specific coordinate without drawing on the way

t.fillcolor("blue")
t.begin_fill()

for i in range(6): # repeat the code 6 times
    t.forward(500)
    t.right(60)

while True: # this turtle will draw forever
    t.forward(500)
    t.right(60)

t.end_fill()

t.done()